# Documentation for src/voiceAssistants/voiceAssistant/main.py

# Command Execution Script Documentation

## Program Overview

The provided Python script is designed to create a command execution system that interacts with an AI model to perform various tasks based on user input. This document will provide an overview of the script's functions and classes, along with explanations and examples.

## Table of Contents

*   [CommandExecution Class](#commandexecution-class)
    *   [Description](#description)
    *   [Methods](#methods)
        *   [__init__](#init)
        *   [setup](#setup)
        *   [decide](#decide)
        *   [find_commands](#find_commands)
        *   [change_name](#change_name)
*   [Main Class](#main-class)
    *   [Description](#description-1)
    *   [Methods](#methods-1)
        *   [__init__](#init-1)
        *   [main_setup](#main_setup)
        *   [get_audio](#get_audio)
        *   [get_input](#get_input)

## Detailed Class Descriptions

### CommandExecution Class

#### Description

The `CommandExecution` class is responsible for handling the execution of commands based on user input and AI responses. It initializes user details, sets up the environment, and decides which commands to execute based on the AI's response.

#### Methods

##### __init__

**Description**: Initializes the `CommandExecution` class and sets up user details.

**Parameters**: None

**Returns**: None

##### setup

**Description**: Sets up the user details and writes them to a file. Also, greets the user.

**Parameters**: None

**Returns**: None

##### decide

**Description**: Decides which commands to execute based on the AI's response. It splits the AI's response into commands and non-commands and executes the appropriate commands.

**Parameters**: None

**Returns**: None

##### find_commands

**Description**: Splits the AI's response into commands and non-commands.

**Parameters**:
    *   `ai_input` (str): The AI's response.

**Returns**:
    *   `command` (list): List of commands.
    *   `non_command` (list): List of non-commands.

##### change_name

**Description**: Changes the user's name and updates the details in the file.

**Parameters**: None

**Returns**: None

### Main Class

#### Description

The `Main` class is responsible for creating the graphical user interface (GUI) and handling user input. It initializes the GUI components and sets up the event handlers for user input.

#### Methods

##### __init__

**Description**: Initializes the `Main` class and sets up the GUI.

**Parameters**: None

**Returns**: None

##### main_setup

**Description**: Sets up the GUI components and initializes the `CommandExecution` class.

**Parameters**: None

**Returns**: None

##### get_audio

**Description**: Handles audio input from the user and passes it to the `CommandExecution` class.

**Parameters**: None

**Returns**: None

##### get_input

**Description**: Handles text input from the user and passes it to the `CommandExecution` class.

**Parameters**: None

**Returns**: None

## Example Usage

### Example Usage of CommandExecution Class

```python
# Initialize the CommandExecution class
command_execution = CommandExecution()

# Set a query
command_execution.query = "change name Jonah Assistant"

# Change the name
command_execution.change_name()
```

### Example Usage of Main Class

```python
# Initialize the Main class
main = Main()

# Simulate user input
main.CommandExecution.query = "open app Chrome"

# Decide and execute the command
main.CommandExecution.decide()
```

This documentation provides a comprehensive overview of the script's functionality, including detailed descriptions of each class and method, along with example usage.