from subprocess import run
import os
from pyWrkspPackage import run_terminal_command
from webbrowser import open as web_open
from urllib.parse import quote

APPLICATION_PATHS = [
    "{}/Applications/".format(os.path.expanduser("~")),
    "/System/Volumes/Preboot/Cryptexes/App/System/Applications/",
    "/System/Applications/",
    "/System/Library/CoreServices/Applications/",
    "/Applications/",
]
PATHS = [os.path.expanduser("~")]


def hide_app(app_name: str) -> None:
    """
    Hide the specified application using AppleScript.

    Parameters:
    app_name (str): The name of the application to hide.
    """
    applescript = f"""
    tell application "{app_name}"
        activate
        delay 0.2
        tell application "System Events" to keystroke "h" using {{command down}}
    end tell
    """
    run(["osascript", "-e", applescript])


def find_path_app(app: str) -> str | bool:
    """
    Find the path of an application using the `mdfind` command.

    Parameters:
    app (str): The name of the application to find.

    Returns:
    str|bool: The path of the application if found, False otherwise.
    """
    search = run_terminal_command('mdfind "{}"'.format(app))
    search = search.split("\n")
    for result in search:
        if (
            (
                (
                    (
                        result.startswith(APPLICATION_PATHS[0])
                        or result.startswith(APPLICATION_PATHS[1])
                    )
                    or (
                        result.startswith(APPLICATION_PATHS[2])
                        or result.startswith(APPLICATION_PATHS[3])
                    )
                )
            )
            or result.startswith(APPLICATION_PATHS[4])
            and result.endswith(".app")
        ):
            return result
    return False


def open_directory_in_finder(directory: str) -> bool:
    """
    Open a directory in Finder.

    Parameters:
    directory (str): The path of the directory to open.

    Returns:
    bool: True if the directory was successfully opened, False otherwise.
    """
    if os.path.isdir(directory):
        run(["open", directory])
        return True
    else:
        return False


def open_app(app: str) -> bool:
    """
    Open an application by its name.

    Parameters:
    app (str): The name of the application to open.

    Returns:
    bool: True if the application was successfully opened, False otherwise.
    """
    app_path = find_path_app(app)
    if not app_path:
        return False
    else:
        run(["open", app_path])
        return True


def find_path(file: str) -> str | bool:
    """
    Find the path of a file using the `mdfind` command.

    Parameters:
    file (str): The name of the file to find.

    Returns:
    str|bool: The path of the file if found, False otherwise.
    """
    file = file.split()
    file_new = ""
    for part in file:
        file_new += part
    file = file_new

    search = run_terminal_command('mdfind "{}"'.format(file))
    if search is None:
        return False
    search = search.split("\n")

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
        print("The file has multiple locations. I haven't implemented this yet.")
        return False


def open_file(file: str) -> bool:
    """
    Open a file using the default application.

    Parameters:
    file (str): The name of the file to open.

    Returns:
    bool: True if the file was successfully opened, False otherwise.
    """
    path = find_path(file)
    if not path:
        return False
    else:
        os.system('open "{}"'.format(path))
        return True


def pause() -> None:
    """
    Pause the music on Spotify.
    """
    run(["osascript", "-e", 'tell application "Spotify" to pause'])


def play(open_spotify=True) -> None:
    """
    Play music on Spotify.

    Parameters:
    open_spotify (bool): If True, open the Spotify application before playing music.
    """
    if open_spotify:
        open_app("Spotify")
    run(["osascript", "-e", 'tell application "Spotify" to play'])
    hide_app("Spotify")


def open_webpage(page: str, https=True) -> None:
    """
    Open a webpage in the default web browser.

    Parameters:
    page (str): The URL or page to open.
    https (bool): If True, prepend 'https://' to the page URL. Defaults to True.
    """
    if https:
        web_open("https://" + page)
    else:
        web_open(page)


def search(query: str) -> str:
    """
    Search for a query on Google.

    Parameters:
    query (str): The search query.

    Returns:
    str: The final URL used for the search.
    """
    base_url = "https://www.duckduckgo.com/?q="
    final_url = base_url + quote(query)
    open_webpage(final_url, https=False)
    return final_url


def terminate() -> None:
    """
    Terminate the program.
    """
    raise KeyboardInterrupt


def quit_app(app: str) -> None:
    """
    Quit an application using AppleScript.

    Parameters:
    app (str): The name of the application to quit.
    """
    applescript = f"""
    tell application "{app}"
        quit
    end tell
    """
    run(["osascript", "-e", applescript])


def set_volume(percentage: int) -> None:
    """
    Set the system volume to a specified percentage.

    Parameters:
    percentage (int): The desired volume level as a percentage (0-100).
    """
    if 0 <= percentage <= 100:
        run(["osascript", "-e", f"set volume output volume {percentage}"])
    else:
        raise ValueError("Volume percentage must be between 0 and 100.")


def get_current_volume() -> int:
    """
    Get the current system volume level.

    Returns:
    int: The current volume level as a percentage (0-100).
    """
    volume = run_terminal_command(
        'osascript -e "output volume of (get volume settings)"'
    )
    return int(volume)
