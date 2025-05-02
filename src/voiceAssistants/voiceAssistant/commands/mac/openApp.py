import os
from commands.mac.runTerminalCommand import run_terminal_command

APPLICATION_PATHS = [
    "/Users/jonahmakowski/Applications/",
    "/System/Volumes/Preboot/Cryptexes/App/System/Applications/",
    "/System/Applications/",
    "/System/Library/CoreServices/Applications/",
    "/Applications/",
]


def find_path_app(app):
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


def open_app(app):
    app_path = find_path_app(app)
    if not app_path:
        return False
    else:
        os.system('open "{}"'.format(app_path))
        return True
