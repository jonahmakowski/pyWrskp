# Documentation for src/helpfulPackage/app/pyWrkspPackage/variable_management.py

# Python Script Documentation

## Program Overview

The provided Python script contains various utility functions designed to perform common tasks such as merging dictionaries, splitting lists into chunks, flattening lists, loading environment variables, converting lists to strings, creating matrices, and recursively copying lists. This document will provide an overview of the script's functions, along with explanations and examples.

## Table of Contents

*   [dict_merge](#dict_merge)
    *   Description: Merges two dictionaries recursively.
    *   Parameters: d1 (dict), d2 (dict)
    *   Returns: dict

*   [chunk_list](#chunk_list)
    *   Description: Splits a list into smaller lists (chunks) of a specified size.
    *   Parameters: lst (list), size (int)
    *   Returns: list

*   [flatten](#flatten)
    *   Description: Flattens a list of lists into a single list.
    *   Parameters: lst (list)
    *   Returns: list

*   [load_from_env](#load_from_env)
    *   Description: Load the value of an environment variable.
    *   Parameters: variable (str)
    *   Returns: str

*   [list_to_str](#list_to_str)
    *   Description: Converts a list of items into a single string with each item separated by a specified separator.
    *   Parameters: lis (list), sep (str, optional)
    *   Returns: str

*   [make_matrix](#make_matrix)
    *   Description: Creates a matrix (2D list) with the specified number of rows and columns.
    *   Parameters: rows (int), cols (int), default (optional)
    *   Returns: list

*   [recursive_copy](#recursive_copy)
    *   Description: Recursively copies a list of lists.
    *   Parameters: lst (list)
    *   Returns: list

## Detailed Function Descriptions

### dict_merge

**Description**: Merges two dictionaries recursively. If a key in both dictionaries has a dictionary as its value, the function will merge those dictionaries as well. Otherwise, the value from the second dictionary will overwrite the value from the first dictionary.

**Parameters**:
    *   d1 (dict): The first dictionary to merge.
    *   d2 (dict): The second dictionary to merge.

**Returns**: dict: The merged dictionary.

### chunk_list

**Description**: Splits a list into smaller lists (chunks) of a specified size.

**Parameters**:
    *   lst (list): The list to be split into chunks.
    *   size (int): The size of each chunk.

**Returns**: list: A list of lists, where each sublist is a chunk of the original list. The last chunk may be smaller if the original list size is not perfectly divisible by the chunk size.

### flatten

**Description**: Flattens a list of lists into a single list.

**Parameters**:
    *   lst (list): A list of lists to be flattened.

**Returns**: list: A single flattened list containing all the elements of the sublists.

### load_from_env

**Description**: Load the value of an environment variable. This function loads the environment variables from a .env file and retrieves the value of the specified environment variable.

**Parameters**:
    *   variable (str): The name of the environment variable to retrieve.

**Returns**: str: The value of the specified environment variable as a string.

### list_to_str

**Description**: Converts a list of items into a single string with each item separated by a specified separator.

**Parameters**:
    *   lis (list): The list of items to be converted to a string.
    *   sep (str, optional): The separator to be used between items. Defaults to an empty string.

**Returns**: str: A single string with all items from the list separated by the specified separator.

### make_matrix

**Description**: Creates a matrix (2D list) with the specified number of rows and columns.

**Parameters**:
    *   rows (int): The number of rows in the matrix.
    *   cols (int): The number of columns in the matrix.
    *   default (optional): The default value to fill the matrix with. Defaults to None.

**Returns**: list: A 2D list representing a matrix with the specified number of rows and columns.

### recursive_copy

**Description**: Recursively copies a list of lists.

**Parameters**:
    *   lst (list): The list to be copied. This can be a nested list.

**Returns**: list: A new list that is a deep copy of the input list.

## Example Usage

### dict_merge

Usage example for `dict_merge`:

```python
d1 = {'a': 1,