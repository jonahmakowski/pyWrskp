from time import sleep
from pygame import mixer
import pyttsx3
from os import remove
import whisper
import speech_recognition as sr

mixer.init()
engine = pyttsx3.init()  # text to speech init
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 1)  # Volume level (0.0 to 1.0)
model = whisper.load_model("base.en")  # Whisper model init


def play_sound(hold: bool, sound="audio/audio.mp3") -> None:
    """
    Play a sound file using the mixer module.

    Args:
        hold (bool): If True, the function will block until the sound finishes playing.
        sound (str, optional): The path to the sound file to play. Defaults to 'audio/audio.mp3'.
    """
    mixer.music.load(sound)
    mixer.music.play()
    if hold:
        while mixer.music.get_busy():
            sleep(0.001)

def speak(message: str, voice=132) -> None:
    """
    Convert text to speech and play it through the speakers.

    Args:
        message (str): The text message to be spoken.
        voice (int, optional): The index of the voice to use. Defaults to 132.
    """
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[voice].id)  # Changing index changes voices
    engine.say(message)
    engine.runAndWait()

def take_command(mic_index) -> str:
    """
    Listens for a voice command and returns the recognized text.

    This function uses the `speech_recognition` library to capture audio from the microphone,
    then processes the audio to recognize and return the spoken text.

    Returns:
        str: The recognized text from the audio input.
    """
    r = sr.Recognizer()

    with sr.Microphone(device_index=mic_index) as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    print("Recognizing...")
    with open("temp_audio.wav", "wb") as f:
        f.write(audio.get_wav_data())
    transcription = model.transcribe("temp_audio.wav")["text"]

    return transcription
