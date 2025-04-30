# Documentation for src/docGeneration/generate.py

# Script Documentation

## Program Overview

This script automates the process of generating documentation for modified Python and C++ source files in a Git repository. It leverages a custom API endpoint to generate documentation using an AI model. The script identifies modified files, filters out relevant source files, removes outdated documentation, and generates new documentation for the modified files.

## Table of Contents

- [Configuration](#configuration)
- [Main Script Workflow](#main-script-workflow)
- [Function Descriptions](#function-descriptions)
  - [get_modified_files](#get_modified_files)
  - [filter_source_files](#filter_source_files)
  - [get_documentation_files](#get_documentation_files)
  - [remove_outdated_documentation](#remove_outdated_documentation)
  - [generate_new_documentation](#generate_new_documentation)
- [Example Usage](#example-usage)

## Configuration

The script requires the following configuration variables:

- `CUSTOM_API_URL`: The URL of the custom API endpoint.
- `OPENAI_API_KEY`: The API key for the OpenAI service or another service.
- `MODEL_NAME`: The name of the model to be used for documentation generation.

```python
CUSTOM_API_URL = "http://192.168.86.4:4001"  # Set your custom API endpoint here
OPENAI_API_KEY = os.getenv("API_KEY")  # Your OpenAI API key or other service's API key
MODEL_NAME = "codestral-latest"  # or other appropriate model name
```

## Main Script Workflow

1. **Get Modified Files**: Retrieve the list of files modified in the last commit.
2. **Filter Source Files**: Filter the modified files to include only Python and C++ source files located in the `src/` directory.
3. **Get Documentation Files**: Retrieve the list of existing documentation files.
4. **Remove Outdated Documentation**: Remove documentation files that correspond to deleted source files.
5. **Generate New Documentation**: Generate new documentation for the modified source files using the custom API endpoint.

## Function Descriptions

### get_modified_files

**Description**: Retrieves the list of files modified in the last commit.

**Parameters**: None

**Returns**: A list of modified files.

```python
def get_modified_files():
    git_diff_cmd = "git diff --name-only HEAD~1"
    modified_files = subprocess.check_output(git_diff_cmd.split()).decode().splitlines()
    return modified_files
```

### filter_source_files

**Description**: Filters the modified files to include only Python and C++ source files located in the `src/` directory.

**Parameters**:
- `modified_files` (list): A list of modified files.

**Returns**: A list of filtered source files.

```python
def filter_source_files(modified_files):
    source_files = [f for f in modified_files if f.startswith("src/") and f.endswith((".py", '.gd'))]
    return source_files
```

### get_documentation_files

**Description**: Retrieves the list of existing documentation files.

**Parameters**: None

**Returns**: A list of documentation files.

```python
def get_documentation_files():
    documentation_files = [os.path.join(dirpath, f) for (dirpath, dirnames, filenames) in os.walk('docs/ai_docs/') for f in filenames]
    return documentation_files
```

### remove_outdated_documentation

**Description**: Removes documentation files that correspond to deleted source files.

**Parameters**:
- `documentation_files` (list): A list of documentation files.

**Returns**: None

```python
def remove_outdated_documentation(documentation_files):
    for doc_file in documentation_files:
        corresponding_source_file = doc_file.replace("docs/ai_docs/", "src/").replace(".md", ".py").replace(".md", ".gd")
        if not os.path.exists(corresponding_source_file):
            print(f"Removing outdated documentation: {doc_file}")
            os.remove(doc_file)
```

### generate_new_documentation

**Description**: Generates new documentation for the modified source files using the custom API endpoint.

**Parameters**:
- `source_files` (list): A list of modified source files.

**Returns**: None

```python
def generate_new_documentation(source_files):
    if not source_files:
        print("No source files modified. Skipping doc generation.")
        return

    client = openai.OpenAI(
        api_key=OPENAI_API_KEY,
        base_url=CUSTOM_API_URL
    )

    for file_num, file in enumerate(source_files):
        if not os.path.exists(file):
            print(f"{file_num} ⚠️ Source file not found: {file}")
            continue

        print(f"{file_num