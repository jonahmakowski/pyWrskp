# Documentation for src/voiceAssistants/voiceAssistant/commands/__init__.py

# Python Script Documentation

## Program Overview

The provided Python script is designed to import and utilize various command modules based on the operating system of the user. It imports different modules for web browsing, image generation, and system-specific commands, with a focus on macOS. If the user's system is not macOS, the script will print a message and exit.

## Table of Contents

- [Function 1](#function-1)
  - Description: Import system specific functions based on the operating system.
  - Parameters: None
  - Returns: None

## Detailed Function Descriptions

### Function 1

#### Description

The script checks the operating system of the user using the `system()` function from the `platform` module. If the system is macOS (Darwin), it imports the `mac` module from the `commands` package. If the system is not supported, it prints a message and exits.

#### Parameters

None

#### Returns

None

## Example Usage

Usage example for the script:

```python
from platform import system
from commands.webBrowser import *
from commands.image_generation import *

# Import system specific functions
if system() == 'Darwin':
    from commands.mac import *
else:
    print('Your system is not supported.')
    raise SystemExit
```

In this example, the script will import the necessary modules based on the user's operating system. If the user is not on macOS, the script will print a message and exit.