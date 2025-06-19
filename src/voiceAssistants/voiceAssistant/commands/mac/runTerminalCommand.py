import subprocess
import commands.mac.openApp as openApp


def run_terminal_command(command):
    result = subprocess.run(
        "{}".format(command), shell=True, capture_output=True, text=True
    )
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return None
