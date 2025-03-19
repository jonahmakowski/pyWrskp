from pyWrkspPackage import *
from os import getenv
from dotenv import load_dotenv
import pvporcupine
from pvrecorder import PvRecorder
from pygame import mixer
from time import sleep
import pyttsx3
import actions
import speech_recognition as sr
from datetime import datetime

# General Setup
load_dotenv()
AI_KEY = getenv('AI_TOKEN')
VOICE_KEY = getenv('VOICE_DETECTION_TOKEN')
AI_MODEL = 'mistral-large-latest'
AI_URL = 'http://192.168.86.4:4001'
SYS_PROMPT = load_from_file('prompt.md')
COMMANDS = {'open-app': [actions.open_app, True], 'search-the-web': [actions.search, True],
            'open-file': [actions.open_file, True], 'play-music': [actions.play, False],
            'pause-music': [actions.pause, False], 'open-webpage': [actions.open_webpage, True],
            'open-folder': [actions.open_directory_in_finder, True], 'hide-application': [actions.hide_app, True],
            'question-mode': ['Question Mode', False]}
USER_NAME = 'Jonah'

# Setting up Audio Systems
mixer.init() # mp3 player init
engine = pyttsx3.init() # text to speech init
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Confirming env variables are set
if AI_KEY is None or VOICE_KEY is None:
    raise ValueError('An environment variable (AI_KEY or VOICE_DETECTION_TOKEN) is not set')

# Define Functions
def play_sound(hold: bool, sound='audio.mp3') -> None:
    """
    Play a sound file using the mixer module.

    Args:
        hold (bool): If True, the function will block until the sound finishes playing.
        sound (str, optional): The path to the sound file to play. Defaults to 'audio.mp3'.
    """
    mixer.music.load(sound)
    mixer.music.play()
    if hold:
        while mixer.music.get_busy():
            sleep(0.001)

def take_command() -> str:
    """
    Listens for a voice command and returns the recognized text.

    This function uses the `speech_recognition` library to capture audio from the microphone,
    then processes the audio to recognize and return the spoken text.

    Returns:
        str: The recognized text from the audio input.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in')

    return query

def get_message_list(cur_list: list, message: str, max_size=10) -> list:
    """
    Update the message list with a new user message.

    Args:
        cur_list (list): The current list of messages.
        message (str): The new user message to add.
        max_size (int, optional): The maximum size of the message list. Defaults to 10.

    Returns:
        list: The updated message list.
    """
    current_datetime = datetime.now()
    cur_date = current_datetime.strftime("%B %d, %Y")
    cur_time = current_datetime.strftime("%I:%M %p")
    if not cur_list:
        return [{"role": "system", "content": SYS_PROMPT.format(cur_date, cur_time, USER_NAME)},
                {"role": "user", "content": message}]
    while len(cur_list) > max_size:
        cur_list.pop(1)
    cur_list[0] = {"role": "system", "content": SYS_PROMPT.format(cur_date, cur_time, USER_NAME)}
    cur_list.append({"role": "user", "content": message})
    return cur_list

def speak(message: str, voice=132) -> None:
    """
    Convert text to speech and play it through the speakers.

    Args:
        message (str): The text message to be spoken.
        voice (int, optional): The index of the voice to use. Defaults to 132.
    """
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)  # Changing index changes voices
    engine.say(message)
    engine.runAndWait()

def parse_command(message: str) -> tuple[str, bool]:
    split_message = message.split('$')
    command = None
    for chunk in split_message:
        for key in COMMANDS.keys():
            if key in chunk:
                del split_message[split_message.index(chunk)]
                command = (COMMANDS[key], chunk)
                break

    if command is None:
        return message, '?' in message

    func = command[0][0]
    if func == 'Question Mode':
        return list_to_str(split_message), True
    elif command[0][1]:
        print('Ran command {} with arguments "{}"'.format(key, list_to_str(command[1].split()[1:], sep=' ')))
        func(list_to_str(command[1].split()[1:], sep=' '))
    else:
        print('Ran command {} without arguments'.format(key))
        func()

    return list_to_str(split_message), False

# Running the actual assistant code
def main():
    porcupine = pvporcupine.create(access_key=VOICE_KEY, keywords=['computer'])
    recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    message_list = []
    question_mode = False

    play_sound(True, 'bootup.mp3')

    try:
        recoder.start()
        while True:
            keyword_index = porcupine.process(recoder.read())
            if keyword_index >= 0 or question_mode:
                recoder.stop()
                play_sound(False)
                try:
                    inp = take_command()
                except sr.UnknownValueError:
                    recoder.start()
                    continue

                message_list = get_message_list(message_list, inp)
                message, message_list = ai_response(message_list, AI_MODEL, AI_URL, AI_KEY)
                print(message)
                speak_version, question_mode = parse_command(message)

                speak(speak_version)

                recoder.start()

    except KeyboardInterrupt:
        recoder.stop()
    finally:
        porcupine.delete()
        recoder.delete()

if __name__ == '__main__':
    main()
