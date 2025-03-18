from pyWrkspPackage import *
from os import getenv
from dotenv import load_dotenv
import pvporcupine
from pvrecorder import PvRecorder
from pygame import mixer
from time import sleep
from actions import *
import speech_recognition as sr

# General Setup
load_dotenv()
AI_KEY = getenv('AI_TOKEN')
VOICE_KEY = getenv('VOICE_DETECTION_TOKEN')
AI_MODEL = 'mistral-large-latest'
AI_URL = 'http://192.168.86.4:4001'
SYS_PROMPT = load_from_file('prompt.md')
mixer.init()

if AI_KEY is None or VOICE_KEY is None:
    raise ValueError('An environment variable (AI_KEY or ) is not set')

# Define Functions
def play_sound(hold: bool) -> None:
    """
    Play a sound from 'audio.mp3'.

    Args:
        hold (bool): If True, the function will block until the sound finishes playing.
    """
    mixer.music.load('audio.mp3')
    mixer.music.play()
    if hold:
        while mixer.music.get_busy():
            sleep(0.001)

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in')

    return query

def get_message_list(cur_list: list, message: str, max_size=10) -> list:
    if not cur_list:
        return [{"role": "system", "content": SYS_PROMPT}, {"role": "user", "content": message}]
    while len(cur_list) > max_size:
        cur_list.pop(0)
    cur_list[0] = {"role": "system", "content": SYS_PROMPT}
    cur_list.append({"role": "user", "content": message})
    return cur_list

# Running the actual assistant code
def main():
    porcupine = pvporcupine.create(access_key=VOICE_KEY, keywords=['computer'])
    recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    message_list = []

    try:
        recoder.start()
        while True:
            keyword_index = porcupine.process(recoder.read())
            if keyword_index >= 0:
                recoder.stop()
                play_sound(False)
                message_list = get_message_list(message_list, take_command())
                message, message_list = ai_response(message_list, AI_MODEL, AI_URL, AI_KEY)
                print(message)
                recoder.start()

    except KeyboardInterrupt:
        recoder.stop()
    finally:
        porcupine.delete()
        recoder.delete()

if __name__ == '__main__':
    main()
