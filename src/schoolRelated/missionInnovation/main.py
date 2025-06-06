import pyaudio
import wave
import whisper
from os import path, getenv, remove
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from time import sleep
from gpiozero import Button, LED
import subprocess
import json


load_dotenv()  # Load environment variables from .env file
EMAIL_PASSWORD = getenv(
    "EMAIL_PASSWORD"
)  # Get email password from environment variable
AI_MODEL = "mistral-large-latest"
button = Button(14)  # GPIO pin for the button
light = LED(15)

whisper_model = whisper.load_model("base.en")  # Whisper model init


def light_on():
    light.on()


def light_off():
    light.off()


def check_button_pressed():
    return button.is_pressed


def record_audio(
    filename="output.wav",
    samplerate=44100,
    channels=1,
    chunk_size=1024,
    record_format=pyaudio.paInt16,
):
    print("Recording...")
    audio = pyaudio.PyAudio()

    # Open stream
    stream = audio.open(
        format=record_format,
        channels=channels,
        rate=samplerate,
        input=True,
        frames_per_buffer=chunk_size,
    )

    frames = []

    try:
        while True:
            if check_button_pressed():
                print("Recording stopped.")
                break
            data = stream.read(chunk_size)
            frames.append(data)
    except KeyboardInterrupt:
        print("Recording interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a file
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(record_format))
        wf.setframerate(samplerate)
        wf.writeframes(b"".join(frames))
    print(f"Audio saved to {filename}")


def transcribe_audio(filename="output.wav"):
    print("Transcribing audio...")
    return whisper_model.transcribe(filename)["text"]


def summarize_audio(transcript):
    print("Summarizing audio...")

    result = subprocess.run(
        ["python3", "generate_summary.py", AI_MODEL],
        input=transcript,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("Subprocess failed:", result.stderr)
        exit(1)
    summary = json.loads(result.stdout)["choices"][0]["message"]["content"]

    return summary


def send_email_with_info(
    summary,
    transcript,
    recipient_emails,
    subject="Lesson Summary",
    audio_file="output.wav",
    sender="pywrkspemail@gmail.com",
):
    print("Sending email with summary and transcription...")
    port = 465

    body = f"Summary:\n{summary}\n\nTranscription:\n{transcript}"

    for receiver_email in recipient_emails:
        print(f"Sending email to {receiver_email}...")
        message = MIMEMultipart("mixed")
        message["From"] = sender
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        # with open(audio_file, "rb") as attachment:
        #    part = MIMEBase("application", "octet-stream")
        #    part.set_payload(attachment.read())

        # encoders.encode_base64(part)

        # part.add_header(
        #    "Content-Disposition",
        #    f"attachment; filename= {audio_file}",
        # )

        # message.attach(part)
        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("pywrkspemail@gmail.com", EMAIL_PASSWORD)
            server.sendmail(sender, receiver_email, text)


def cleanup():
    if path.exists("output.wav"):
        print("Removing output.wav...")
        remove("output.wav")
    print("Cleanup complete.")


if __name__ == "__main__":
    emails = ["jonah@makowski.ca"]
    while True:
        light_off()
        print("Press the button to start recording...")
        while not check_button_pressed():
            sleep(0.1)
        print("Button pressed, waiting for release...")
        while check_button_pressed():
            light_on()
            sleep(0.5)
            light_off()
        print("Button released, starting recording...")

        light_on()
        record_audio()
        light_off()

        transcript = transcribe_audio()
        print(f"Transcription: {transcript}")

        summary = summarize_audio(transcript)
        print(f"Summary: {summary}")

        send_email_with_info(summary, transcript, emails)

        cleanup()
