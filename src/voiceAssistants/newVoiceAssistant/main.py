from pyWrkspPackage import list_to_str, ai_response, load_from_file
from helper import *
import actions
from os import getenv
from dotenv import load_dotenv
import pvporcupine
from pvrecorder import PvRecorder
import speech_recognition as sr
from datetime import datetime
from pandas.io.clipboard import paste
import spotify_runner

# General Setup
load_dotenv()
AI_KEY = getenv('AI_TOKEN')
VOICE_KEY = getenv('VOICE_DETECTION_TOKEN')
AI_MODEL = getenv('AI_MODEL')
AI_URL = getenv('AI_URL')
SYS_PROMPT = load_from_file('prompt.md')
# Commands dictionary format: {ai_command: [function, requires_arguments]}
COMMANDS = {'open-app': [actions.open_app, True], 'search-the-web': [actions.search, True],
            'open-file': [actions.open_file, True], 'spotify': [spotify_runner.do_spotify, True, True], 'open-webpage': [actions.open_webpage, True],
            'open-folder': [actions.open_directory_in_finder, True], 'hide-application': [actions.hide_app, True],
            'question-mode': ['Question Mode', False], 'clipboard-contents': [paste, False], 'terminate': [actions.terminate, False],
            'quit-application': [actions.quit_app, True]}
USER_NAME = 'Jonah'

# Confirming env variables are set
if AI_KEY is None or VOICE_KEY is None:
    raise ValueError('An environment variable (AI_KEY or VOICE_DETECTION_TOKEN) is not set')

# Define Functions
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
        return [{"role": "system", "content": SYS_PROMPT.format(cur_date, cur_time, USER_NAME, AI_MODEL)},
                {"role": "user", "content": message}]
    while len(cur_list) > max_size:
        cur_list.pop(0)
    cur_list[0] = {"role": "system", "content": SYS_PROMPT.format(cur_date, cur_time, USER_NAME, AI_MODEL)}
    cur_list.append({"role": "user", "content": message})
    return cur_list

def parse_command(message: str, message_list: list) -> tuple[str, bool]:
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
    elif len(command[0]) == 3:
        func(list_to_str(split_message))
    elif func == paste:
        print('Ran command {} without arguments'.format(key))
        speak(command[1].split()[0])
        clipboard = str(paste())
        print(clipboard)
        message_list = get_message_list(message_list, 'AUTOMATED RESPONSE: Clipboard contents: {}'.format(clipboard))
        print(message_list)
        response, message_list = ai_response(message_list, AI_MODEL, AI_URL, AI_KEY, stream=False)
        return response, False
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
                prev_volume = actions.get_current_volume()
                play_sound(True)
                actions.set_volume(0)
                try:
                    inp = take_command()
                except sr.UnknownValueError:
                    recoder.start()
                    continue
                actions.set_volume(prev_volume)

                message_list = get_message_list(message_list, inp)
                message, message_list = ai_response(message_list, AI_MODEL, AI_URL, AI_KEY)
                print(message)
                speak_version, question_mode = parse_command(message, message_list)

                speak(speak_version)

                recoder.start()

    except KeyboardInterrupt:
        recoder.stop()
    finally:
        porcupine.delete()
        recoder.delete()

if __name__ == '__main__':
    main()
