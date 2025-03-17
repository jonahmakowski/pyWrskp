import commands.mac.openApp as openApp
import subprocess
import commands.mac.appUtils as appUtils


def pause():
    subprocess.run(['osascript', '-e', 'tell application "Spotify" to pause'])


def play(open_spotify=True):
    if open_spotify:
        openApp.open_app('Spotify')
    subprocess.run(['osascript', '-e', 'tell application "Spotify" to play'])
    appUtils.hide_app('Spotify')
