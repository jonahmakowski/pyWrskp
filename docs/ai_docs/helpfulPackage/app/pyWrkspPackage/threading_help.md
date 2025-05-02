# Documentation for src/helpfulPackage/app/pyWrkspPackage/threading_help.py

# Python Script Documentation

## Program Overview

This script provides utilities for running functions in separate threads and importing Python modules or submodules in parallel. It includes functions to run functions in threads, retrieve their results, and import packages asynchronously.

## Table of Contents

* [run_in_thread](#run_in_thread)
    * Description: Runs a function in a separate thread.
    * Parameters: `func`, `*args`, `**kwargs`
    * Returns: `threading.Thread`

* [run_in_thread_with_return](#run_in_thread_with_return)
    * Description: Runs a function in a separate thread and returns the result.
    * Parameters: `func`, `*args`, `**kwargs`
    * Returns: `threading.Thread`, `threading.Event`

* [run_imports_in_thread](#run_imports_in_thread)
    * Description: Imports Python modules or submodules in separate threads and updates the global namespace with the imported modules using specified aliases.
    * Parameters: `packages`, `aliases`
    * Returns: `None`

## Detailed Function Descriptions

### run_in_thread

**Description**: Runs a function in a separate thread.

**Parameters**:
* `func` (callable): The function to run.
* `*args`: Positional arguments to pass to the function.
* `**kwargs`: Keyword arguments to pass to the function.

**Returns**: `threading.Thread`: The thread object running the function.

**Example Usage**:
```python
def example_function(x, y):
    return x + y

thread = run_in_thread(example_function, 5, y=3)
```

### run_in_thread_with_return

**Description**: Runs a function in a separate thread and returns the result.

**Parameters**:
* `func` (callable): The function to run.
* `*args`: Positional arguments to pass to the function.
* `**kwargs`: Keyword arguments to pass to the function.

**Returns**: `threading.Thread`, `threading.Event`: The thread object running the function and an event to wait for the result.

**Example Usage**:
```python
def example_function(x, y):
    return x + y

result_container, thread = run_in_thread_with_return(example_function, 5, y=3)
thread.join()
print(result_container["result"])  # Output: 8
```

### run_imports_in_thread

**Description**: Imports Python modules or submodules in separate threads and updates the global namespace with the imported modules using specified aliases.

**Parameters**:
* `packages` (list): A list of packages to import. Each element can be:
    * A string representing the package name (e.g., "os").
    * A tuple where the first element is the package name and the second element is the submodule name (e.g., ("os", "path")).
* `aliases` (list | None, optional): A list of aliases corresponding to the `packages` list. Each alias can be:
    * A string representing the alias for the package (e.g., "os_alias").
    * A tuple where the second element is the alias for the submodule (e.g., ("os", "path_alias")).
    * Defaults to `None`, in which case the package names are used as aliases.

**Behavior**:
* Each package or submodule is imported in a separate thread.
* The imported modules or submodules are added to the global namespace with the specified aliases.
* Prints a message for each imported module or submodule in the format: "Imported <alias> as <package_name>".

**Raises**:
* `IndexError`: If the length of `aliases` does not match the length of `packages`.

**Example Usage**:
```python
packages = ["os", ("os", "path")]
aliases = ["os_alias", ("os", "path_alias")]
run_imports_in_thread(packages, aliases)
# Imports the `os` module as `os_alias` and the `os.path` submodule as `path_alias`.
```

## Example Usage

### Example 1: Running a Function in a Thread

```python
def example_function(x, y):
    return x + y

thread = run_in_thread(example_function, 5, y=3)
```

### Example 2: Running a Function in a Thread and Retrieving the Result

```python
def example_function(x, y):
    return x + y

result_container, thread = run_in_thread_with_return(example_function, 5, y=3)
thread.join()
print(result_container["result"])  # Output: 8
```

### Example 3: Importing Packages in Threads

```python
packages = ["os", ("os", "path")]
aliases = ["os_alias", ("os", "path