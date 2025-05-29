from helper import *
from os import getenv
from dotenv import load_dotenv
from pvrecorder import PvRecorder
import pvporcupine
import speech_recognition as sr

load_dotenv()
VOICE_KEY = getenv("VOICE_DETECTION_TOKEN")


def main():
    porcupine = pvporcupine.create(access_key=VOICE_KEY, keywords=["jarvis"])
    devices = PvRecorder.get_available_devices()
    print("Available devices:")
    for index, device in enumerate(devices):
        print(f"{index}: {device}")

    device_index = int(input("Select the device index: "))

    mic_list = sr.Microphone.list_microphone_names()
    print("Available microphones:")
    for i, mic_name in enumerate(mic_list):
        print(f"{i}: {mic_name}")

    mic_index = int(input("Enter the index of the microphone you want to use: "))

    recoder = PvRecorder(device_index=device_index, frame_length=porcupine.frame_length)

    play_sound(True, "audio/bootup.mp3")

    try:
        recoder.start()
        while True:
            keyword_index = porcupine.process(recoder.read())
            if keyword_index >= 0:
                play_sound(False)
                transcription = take_command(mic_index)
                print(transcription)

    except KeyboardInterrupt:
        recoder.stop()
    finally:
        porcupine.delete()
        recoder.delete()


if __name__ == "__main__":
    main()
