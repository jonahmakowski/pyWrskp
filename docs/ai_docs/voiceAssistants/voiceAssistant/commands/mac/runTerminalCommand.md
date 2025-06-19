# Documentation for src/voiceAssistants/voiceAssistant/commands/mac/runTerminalCommand.py

# Python Script Documentation

## Program Overview

The provided Python script is designed to execute terminal commands using the `subprocess` module. It also uses a custom module `commands.mac.openApp` to open applications on macOS. This document will provide an overview of the script's functions and classes, along with explanations and examples.

## Table of Contents

*   [run_terminal_command](#run_terminal_command)
    *   Description: Executes a terminal command and returns the output.
    *   Parameters: The command to be executed.
    *   Returns: The output of the command if successful, otherwise None.

## Detailed Function Descriptions

### run_terminal_command

Description: This function executes a terminal command using the `subprocess.run` method. It captures the output of the command and returns it if the command is successful. If the command fails, it returns None.

Parameters:
    *   command (str): The terminal command to be executed.

Returns: The output of the command if successful, otherwise None.

## Example Usage

Usage example for `run_terminal_command`:

```python
# Import the function
from your_script import run_terminal_command

# Define the command to be executed
command = "ls -l"

# Execute the command and get the output
output = run_terminal_command(command)

# Print the output
print(output)
```

In this example, the `run_terminal_command` function is used to list the contents of the current directory in long format. The output is then printed to the console.