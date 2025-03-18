# Documentation for src/newVoiceAssistant/main.py

# Python Script Documentation

## Program Overview

The provided Python script is designed to create a command execution system that interacts with a user through text input and audio commands. It utilizes various modules such as `llama_ai`, `commands`, `audio`, and `helpers` to perform different tasks based on user input. The script also includes a graphical user interface (GUI) built with `tkinter` for user interaction.

## Table of Contents

- [CommandExecution Class](#commandexecution-class)
  - [Description](#description)
  - [Methods](#methods)
    - [__init__](#init)
    - [setup](#setup)
    - [decide](#decide)
    - [find_commands](#find_commands)
    - [change_name](#change_name)

- [Main Class](#main-class)
  - [Description](#description-1)
  - [Methods](#methods-1)
    - [__init__](#init-1)
    - [main_setup](#main_setup)
    - [get_audio](#get_audio)
    - [get_input](#get_input)

- [Example Usage](#example-usage)

## CommandExecution Class

### Description

The `CommandExecution` class handles the execution of commands based on user input. It initializes user details, processes AI responses, and executes commands accordingly.

### Methods

#### __init__

**Description:** Initializes the `CommandExecution` object and calls the `setup` method.

**Parameters:** None

**Returns:** None

#### setup

**Description:** Sets up initial user details and writes them to a file. Also, greets the user.

**Parameters:** None

**Returns:** None

#### decide

**Description:** Processes the user query, gets AI response, and executes the appropriate commands.

**Parameters:** None

**Returns:** None

#### find_commands

**Description:** Extracts commands and non-command parts from the AI response.

**Parameters:**
- `ai_input` (str): The input string from the AI.

**Returns:**
- `command` (list): List of commands.
- `non_command` (list): List of non-command parts.

#### change_name

**Description:** Changes the user's name and assistant's name based on the user query.

**Parameters:** None

**Returns:** None

## Main Class

### Description

The `Main` class sets up the GUI and handles user interactions. It initializes the `CommandExecution` object and processes user input through text or audio.

### Methods

#### __init__

**Description:** Initializes the `Main` object and calls the `main_setup` method.

**Parameters:** None

**Returns:** None

#### main_setup

**Description:** Sets up the GUI components using `tkinter`.

**Parameters:** None

**Returns:** None

#### get_audio

**Description:** Captures audio input from the user, processes it, and decides on the appropriate action.

**Parameters:** None

**Returns:** None

#### get_input

**Description:** Captures text input from the user, processes it, and decides on the appropriate action.

**Parameters:** None

**Returns:** None

## Example Usage

### Example Usage for CommandExecution Class

```python
# Initialize the CommandExecution object
command_execution = CommandExecution()

# Set a query and decide on the appropriate action
command_execution.query = "change name Jonah Assistant"
command_execution.decide()
```

### Example Usage for Main Class

```python
# Initialize the Main object
main = Main()

# Simulate getting audio input
main.get_audio()

# Simulate getting text input
main.get_input()
```

This documentation provides a comprehensive overview of the script's functionality, including detailed descriptions of each function and class, along with usage examples.