# Documentation for src/programmingLanguage/commands.py

# Python Script Documentation

## Program Overview

The provided script defines a set of classes and methods to handle various commands, such as loading files, printing messages, speaking messages, and performing arithmetic operations. Each command is encapsulated within its own class, inheriting from a base `Command` class. The script also handles custom error management and dynamic imports.

## Table of Contents

- [Command Class](#command-class)
  - [Description](#description)
  - [Methods](#methods)
    - [\_\_init\_\_](#__init__)
    - [\_\_str\_\_](#__str__)
    - [\_\_repr\_\_](#__repr__)
    - [impo](#impo)
- [LoadFile Class](#loadfile-class)
  - [Description](#description-1)
  - [Methods](#methods-1)
    - [\_\_init\_\_](#__init__-1)
    - [load_params](#load_params)
    - [execute](#execute)
    - [impo](#impo-1)
- [Print Class](#print-class)
  - [Description](#description-2)
  - [Methods](#methods-2)
    - [\_\_init\_\_](#__init__-2)
    - [load_params](#load_params-1)
    - [execute](#execute-1)
- [Say Class](#say-class)
  - [Description](#description-3)
  - [Methods](#methods-3)
    - [\_\_init\_\_](#__init__-3)
    - [load_params](#load_params-2)
    - [execute](#execute-2)
    - [impo](#impo-2)
- [Add Class](#add-class)
  - [Description](#description-4)
  - [Methods](#methods-4)
    - [\_\_init\_\_](#__init__-4)
    - [load_params](#load_params-3)
    - [execute](#execute-3)
- [Sub Class](#sub-class)
  - [Description](#description-5)
  - [Methods](#methods-5)
    - [\_\_init\_\_](#__init__-5)
    - [load_params](#load_params-4)
    - [execute](#execute-4)
- [Mult Class](#mult-class)
  - [Description](#description-6)
  - [Methods](#methods-6)
    - [\_\_init\_\_](#__init__-6)
    - [load_params](#load_params-5)
    - [execute](#execute-5)
- [Div Class](#div-class)
  - [Description](#description-7)
  - [Methods](#methods-7)
    - [\_\_init\_\_](#__init__-7)
    - [load_params](#load_params-6)
    - [execute](#execute-6)

## Detailed Function Descriptions

### Command Class

**Description**: The base class for all command classes. It initializes the command with a description, name, and import status.

**Methods**:

#### __init__

**Description**: Initializes the command with a description, name, and import status.
**Parameters**:
- `description` (str): A brief description of the command.
- `name` (str): The name of the command.
- `imp` (bool): A boolean indicating whether the command is imported.

**Returns**: None

#### __str__

**Description**: Returns a string representation of the command.
**Parameters**: None
**Returns**: A string representation of the command.

#### __repr__

**Description**: Returns a string representation of the command.
**Parameters**: None
**Returns**: A string representation of the command.

#### impo

**Description**: Checks if the command is imported. If not, raises a `NotImplementedError`.
**Parameters**: None
**Returns**: None

### LoadFile Class

**Description**: A command class to load a file from the filesystem.

**Methods**:

#### __init__

**Description**: Initializes the `LoadFile` command.
**Parameters**: None
**Returns**: None

#### load_params

**Description**: Loads the file path parameter.
**Parameters**:
- `file_path` (str): The path to the file to be loaded.
**Returns**: None

#### execute

**Description**: Executes the command to load the file.
**Parameters**: None
**Returns**: The content of the loaded file.

#### impo

**Description**: Imports the `load_from_file` function if not already imported.
**Parameters**: None
**Returns**: None

### Print Class

**Description**: A command class to print a message to the console.

**Methods**:

#### __init__

**Description**: Initializes the `Print` command.
**Parameters**: None
**Returns**: None

#### load_params

**Description**: Loads the parameters for