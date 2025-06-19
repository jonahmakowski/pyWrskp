import subprocess


def hide_app(app_name):
    applescript = f"""
    tell application "{app_name}"
        activate
        delay 0.2
        tell application "System Events" to keystroke "h" using {{command down}}
    end tell
    """
    subprocess.run(["osascript", "-e", applescript])
