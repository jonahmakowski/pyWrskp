from shutil import get_terminal_size
from subprocess import run as subprocess_run
import helpers
import commands.mac.playPause as playPause


def replace_with_username(text):
    username_speak = helpers.get_details()[1]
    username_write = helpers.get_details()[0]

    text_list = text.split()
    speak_list = []
    write_list = []

    for item in text_list:
        if "{{USERNAME}}" in item:
            speak_list.append(item.replace("{{USERNAME}}", username_speak))
            write_list.append(item.replace("{{USERNAME}}", username_write))
        else:
            speak_list.append(item)
            write_list.append(item)

    new_write = ""
    new_speak = ""

    for word in write_list:
        new_write += word + " "

    for word in speak_list:
        new_speak += word + " "

    new_write = new_write[:-1]
    new_speak = new_speak[:-1]

    return new_write, new_speak


def speak(text):
    write, talk = replace_with_username(text)
    subprocess_run(["say", talk])
