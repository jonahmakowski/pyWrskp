# Documentation for src/programmingLanguage/parser.py

# Documentation for Script

## Program Overview

The provided script is designed to parse and execute commands from a file written in a custom scripting language. It supports variable assignment, command execution, and multithreaded command imports. The script leverages the `commands` and `errors` modules to define available commands and handle errors, respectively.

## Table of Contents

- [Function 1: `get_tokens`](#function-1-get_tokens)
  - Description: Tokenizes a line of code by splitting it into individual components.
  - Parameters: `line` (str)
  - Returns: `tokens` (list)

- [Function 2: `parse_line`](#function-2-parse_line)
  - Description: Parses a single line of code, handling variable substitution and command execution.
  - Parameters: `line` (str)
  - Returns: None

- [Function 3: `parse_file`](#function-3-parse_file)
  - Description: Parses a file containing custom scripting language commands and executes them.
  - Parameters: `file_path` (str)
  - Returns: None

- [Global Variables](#global-variables)
  - Description: Global variables used to store available commands and variables.

## Detailed Function Descriptions

### Function 1: `get_tokens`

**Description**: Tokenizes a line of code by splitting it into individual components. It removes comments and empty tokens.

**Parameters**:
- `line` (str): The line of code to be tokenized.

**Returns**: `tokens` (list): A list of tokens extracted from the line.

**Example Usage**:
```python
line = "var1 = 10 # This is a comment"
tokens = get_tokens(line)
print(tokens)  # Output: ['var1', '=', '10']
```

### Function 2: `parse_line`

**Description**: Parses a single line of code, handling variable substitution and command execution. It updates the global `variables` dictionary with new variable assignments and executes commands.

**Parameters**:
- `line` (str): The line of code to be parsed.

**Returns**: None

**Example Usage**:
```python
line = "var1 = 10"
parse_line(line)
print(variables)  # Output: {'var1': {'value': 10, 'type': 'int'}}
```

### Function 3: `parse_file`

**Description**: Parses a file containing custom scripting language commands and executes them. It supports multithreaded command imports and handles variable assignments.

**Parameters**:
- `file_path` (str): The path to the file to be parsed.

**Returns**: None

**Example Usage**:
```python
parse_file('example.jonahscript')
print(variables)  # Output: The variables dictionary after parsing the file
```

## Global Variables

### `commands_avalible_direct`

**Description**: A list of dictionaries containing available command classes and their names.

**Example**:
```python
commands_avalible_direct = [
    {'exec': <class 'commands.Command1'>, 'name': 'Command1'},
    {'exec': <class 'commands.Command2'>, 'name': 'Command2'}
]
```

### `commands_avalible`

**Description**: A dictionary mapping command names to their corresponding command classes.

**Example**:
```python
commands_avalible = {
    'Command1': <class 'commands.Command1'>,
    'Command2': <class 'commands.Command2'>
}
```

### `variables`

**Description**: A dictionary storing variable names, their values, and types.

**Example**:
```python
variables = {
    'var1': {'value': 10, 'type': 'int'},
    'var2': {'value': 'hello', 'type': 'str'}
}
```

## Example Usage

Here is an example of how to use the script to parse and execute commands from a file:

```python
if __name__ == "__main__":
    parse_file('example.jonahscript')
    print(variables)
```

This will parse the `example.jonahscript` file, execute the commands, and print the resulting variables.