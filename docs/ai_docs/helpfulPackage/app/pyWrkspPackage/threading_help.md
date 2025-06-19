# Documentation for src/helpfulPackage/app/pyWrkspPackage/threading_help.py

# Threading and Importing Utilities

This script provides utilities for running functions in separate threads and for importing Python modules or submodules in separate threads. The script includes functions for running functions in threads, running functions in threads with return values, and importing packages in threads with specified aliases.

## Table of Contents

- [Function: `run_in_thread`](#function-run_in_thread)
- [Function: `run_in_thread_with_return`](#function-run_in_thread_with_return)
- [Function: `run_imports_in_thread`](#function-run_imports_in_thread)
  - [Nested Function: `import_packages`](#nested-function-import_packages)

## Detailed Function Descriptions

### Function: `run_in_thread`

**Description:** Runs a function in a separate thread.

**Parameters:**
- `func` (callable): The function to run.
- `*args`: Positional arguments to pass to the function.
- `**kwargs`: Keyword arguments to pass to the function.

**Returns:** `threading.Thread`: The thread object running the function.

**Example Usage:**

```python
def example_function(x, y):
    print(f"Result: {x + y}")

thread = run_in_thread(example_function, 1, 2)
thread.join()  # Wait for the thread to complete
```

### Function: `run_in_thread_with_return`

**Description:** Runs a function in a separate thread and returns the result.

**Parameters:**
- `func` (callable): The function to run.
- `*args`: Positional arguments to pass to the function.
- `**kwargs`: Keyword arguments to pass to the function.

**Returns:** `threading.Thread, threading.Event`: The thread object running the function and an event to wait for the result.

**Example Usage:**

```python
def example_function(x, y):
    return x + y

result_container, thread = run_in_thread_with_return(example_function, 1, 2)
thread.join()  # Wait for the thread to complete
print(f"Result: {result_container['result']}")
```

### Function: `run_imports_in_thread`

**Description:** Imports Python modules or submodules in separate threads and updates the global namespace with the imported modules using specified aliases.

**Parameters:**
- `packages` (list): A list of packages to import. Each element can be:
  - A string representing the package name (e.g., `"os"`).
  - A tuple where the first element is the package name and the second element is the submodule name (e.g., `("os", "path")`).
- `aliases` (list | None, optional): A list of aliases corresponding to the `packages` list. Each alias can be:
  - A string representing the alias for the package (e.g., `"os_alias"`).
  - A tuple where the second element is the alias for the submodule (e.g., `("os", "path_alias")`).
  Defaults to `None`, in which case the package names are used as aliases.

**Behavior:**
- Each package or submodule is imported in a separate thread.
- The imported modules or submodules are added to the global namespace with the specified aliases.
- Prints a message for each imported module or submodule in the format: `"Imported <alias> as <package_name>"`.

**Raises:**
- `IndexError`: If the length of `aliases` does not match the length of `packages`.

**Example Usage:**

```python
packages = ["os", ("os", "path")]
aliases = ["os_alias", ("os", "path_alias")]
run_imports_in_thread(packages, aliases)
# Imports the `os` module as `os_alias` and the `os.path` submodule as `path_alias`.
```

#### Nested Function: `import_packages`

**Description:** Dynamically imports a module or submodule and associates it with an alias.

**Parameters:**
- `alias` (str): The alias to associate with the imported module or submodule.
- `package` (str | tuple): The name of the module to import as a string, or a tuple where the first element is the module name and the second element is the submodule name.

**Returns:** `dict`: A dictionary containing the alias and the imported module or submodule. The dictionary has the following structure:
```python
{
    "alias": <alias>,
    "package": <imported module or submodule>
}
```

**Raises:**
- `ImportError`: If the specified module or submodule cannot be imported.
- `AttributeError`: If the specified submodule does not exist in the module.

**Example Usage:**

```python
result = import_packages("os_alias", "os")
print(result)  # {'alias