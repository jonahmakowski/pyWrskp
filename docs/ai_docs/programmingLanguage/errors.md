# Documentation for src/programmingLanguage/errors.py

# Documentation for Error Handling Classes

This document provides an overview of the error handling classes defined in the provided script. These classes are designed to handle various types of errors related to user actions and language limitations.

## Table of Contents

- [UserError](#usererror)
  - [FileNotFoundError](#filenotfounderror)
  - [CommandNotFoundError](#commandnotfounderror)
  - [VariableNotFoundError](#variablenotfounderror)
  - [SyntaxError](#syntaxerror)
- [LanguageError](#languageerror)
  - [NotImplementedError](#notimplementederror)
  - [NotImportedError](#notimportederror)
  - [UnkownError](#unkownerror)

## Detailed Class Descriptions

### UserError

**Description**: Base class for user-related errors.

**Parameters**:
- `type` (str): The type of the error.
- `message` (str): The error message.

**Returns**: None

**Example Usage**:

```python
raise UserError("CustomError", "This is a custom error message.")
```

### FileNotFoundError

**Description**: Exception raised when a file is not found.

**Parameters**:
- `filename` (str): The name of the file that was not found.

**Returns**: None

**Example Usage**:

```python
raise FileNotFoundError("example.txt")
```

### CommandNotFoundError

**Description**: Exception raised when a command is not found.

**Parameters**:
- `command` (str): The command that was not found.

**Returns**: None

**Example Usage**:

```python
raise CommandNotFoundError("ls")
```

### VariableNotFoundError

**Description**: Exception raised when a variable is not found.

**Parameters**:
- `variable` (str): The variable that was not found.

**Returns**: None

**Example Usage**:

```python
raise VariableNotFoundError("my_variable")
```

### SyntaxError

**Description**: Exception raised for syntax errors.

**Parameters**:
- `message` (str): The error message.

**Returns**: None

**Example Usage**:

```python
raise SyntaxError("Invalid syntax detected.")
```

### LanguageError

**Description**: Exception raised for language-related errors.

**Parameters**:
- `message` (str): The error message.

**Returns**: None

**Example Usage**:

```python
raise LanguageError("This is a language-related error.")
```

### NotImplementedError

**Description**: Exception raised when a feature is not implemented.

**Parameters**:
- `feature` (str): The feature that is not implemented.

**Returns**: None

**Example Usage**:

```python
raise NotImplementedError("Advanced feature")
```

### NotImportedError

**Description**: Exception raised when a feature is not imported.

**Parameters**:
- `feature` (str): The feature that is not imported.

**Returns**: None

**Example Usage**:

```python
raise NotImportedError("External library")
```

### UnkownError

**Description**: Exception raised for unknown errors.

**Parameters**:
- `message` (str): The error message.

**Returns**: None

**Example Usage**:

```python
raise UnkownError("An unknown error occurred.")
```