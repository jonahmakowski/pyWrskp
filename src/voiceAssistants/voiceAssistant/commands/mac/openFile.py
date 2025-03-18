import os
from commands.mac.runTerminalCommand import run_terminal_command
import audio
import PySimpleGUI as sg

PATHS = [os.path.expanduser("~")]


def find_path(file):
    file = file.split()
    file_new = ''
    for part in file:
        file_new += part
    file = file_new

    search = run_terminal_command('mdfind "{}"'.format(file))
    if search is None:
        return False
    search = search.split('\n')

    in_path_searches = []

    for result in search:
        for path in PATHS:
            if result.startswith(path):
                in_path_searches.append(result)

    if len(in_path_searches) == 0:
        return False
    elif len(in_path_searches) == 1:
        return in_path_searches[0]
    else:
        audio.speak('The file {} has several results, which would you like to open?'.format(file))
        window = sg.Window('Choose a path',
                           [[sg.Combo(in_path_searches, readonly=True, default_value=in_path_searches[0])],
                            [sg.Button('Ok')]])
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                return False
            elif event == 'Ok':
                return str(values[0])


def open_file(file):
    path = find_path(file)
    if not path:
        return False
    else:
        os.system('open "{}"'.format(path))
        return True
