from platform import system
from commands.webBrowser import *
from commands.image_generation import *

# Import system specific functions
if system() == "Darwin":
    from commands.mac import *
else:
    print("Your system is not supported.")
    raise SystemExit
