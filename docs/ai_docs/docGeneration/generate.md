# Documentation for src/docGeneration/generate.py

# AI Summary
This file is responsible for generating documentation for modified source files. It retrieves a list of modified files, filters them to only include source files, removes outdated documentation, and generates new documentation for the modified source files.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 7/10

The reason for the AI's rating is:

The code is generally well-structured and easy to understand. However, there are a few areas where the code could be improved for better readability and maintainability. For example, the function names could be more descriptive, and some of the string manipulations could be simplified.
# Functions

## get_modified_files
### Explanation
This function retrieves a list of files that have been modified in the last commit. It uses the git diff command to get the list of modified files and then splits the output into a list of file paths.
### Code
```python
def get_modified_files():
    git_diff_cmd = "git diff --name-only HEAD~1"
    modified_files = subprocess.check_output(git_diff_cmd.split()).decode().splitlines()
    return modified_files
```

## filter_source_files
### Explanation
This function filters the list of modified files to only include files from the /src/ directory that have Python or C++ file extensions.
### Code
```python
def filter_source_files(modified_files):
    source_files = [
        f
        for f in modified_files
        if f.startswith("src/") and f.endswith((".py", ".gd", ".cpp", ".rs", ".c", ".h"))
    ]
    return source_files
```

## get_documentation_files
### Explanation
This function retrieves a list of documentation files from the /docs/ai_docs/ directory.
### Code
```python
def get_documentation_files():
    documentation_files = [
        os.path.join(dirpath, f)
        for (dirpath, dirnames, filenames) in os.walk("docs/ai_docs/")
        for f in filenames
    ]
    return documentation_files
```

## remove_outdated_documentation
### Explanation
This function removes outdated documentation files. It checks if the corresponding source file exists for each documentation file. If the source file does not exist, the documentation file is removed.
### Code
```python
def remove_outdated_documentation(documentation_files):
    for doc_file in documentation_files:
        corresponding_source_file = (
            doc_file.replace(".md", ".py")
            .replace(".markdown", ".gd")
            .replace(".cpp.md", ".cpp")
            .replace(".rs.md", ".rs")
            .replace(".c.md", ".c")
            .replace(".h.md", ".h")
        )
        corresponding_source_file = "src/" + doc_file.split("/", 2)[2]

        if not os.path.exists(corresponding_source_file):
            print(f"Removing outdated documentation: {doc_file}")
            os.remove(doc_file)
```

## generate_documentation
### Explanation
This function generates documentation for the modified source files. It uses the new_n8n_version.get_summary function to generate the documentation. The documentation is then written to a file in the /docs/ai_docs/ directory with the corresponding file path and .md extension.
### Code
```python
def generate_documentation(source_files):
    if not source_files:
        print("No source files modified. Skipping doc generation.")
        exit(0)

    for file_num, file in enumerate(source_files):
        if not os.path.exists(file):
            print(f"{file_num} ⚠️ Source file not found: {file}")
            continue

        print(f"{file_num} Generating docs for: {file}")

        documentation = new_n8n_version.get_summary(file)

        # Convert file path from /src/ to /docs/
        doc_path = "docs/ai_docs/" + file.split("/", 1)[1]

        # Change the file extension to .md
        doc_path = (
            doc_path.replace(".py", ".md")
            .replace(".gd", ".markdown")
            .replace(".cpp", ".cpp.md")
            .replace(".rs", ".rs.md")
            .replace(".c", ".c.md")
            .replace(".h", ".h.md")
        )

        # Ensure parent directories exist
        os.makedirs(os.path.dirname(doc_path), exist_ok=True)

        # Write the documentation to the mirrored docs folder
        with open(doc_path, "w") as f:
            f.write(f"# Documentation for {file}\n\n{documentation}")

        print(f"✅ Saved docs: {doc_path}")
```
# Overall File Contents
```python
import os
import subprocess
import new_n8n_version

# Get list of modified files in the last commit
git_diff_cmd = "git diff --name-only HEAD~1"
modified_files = subprocess.check_output(git_diff_cmd.split()).decode().splitlines()

print("Modified files:", modified_files)

# Filter files from /src/ that are Python or C++ source_files
source_files = [
    f
    for f in modified_files
    if f.startswith("src/") and f.endswith((".py", ".gd", ".cpp", ".rs", ".c", ".h"))
]

print(f"{len(source_files)}; Source files:", source_files)

documentation_files = [
    os.path.join(dirpath, f)
    for (dirpath, dirnames, filenames) in os.walk("docs/ai_docs/")
    for f in filenames
]
print(f"{len(documentation_files)}; Documentation files:", documentation_files)

# Remove old documentation for files that have been deleted
for doc_file in documentation_files:
    corresponding_source_file = (
        doc_file.replace(".md", ".py")
        .replace(".markdown", ".gd")
        .replace(".cpp.md", ".cpp")
        .replace(".rs.md", ".rs")
        .replace(".c.md", ".c")
        .replace(".h.md", ".h")
    )
    corresponding_source_file = "src/" + doc_file.split("/", 2)[2]

    if not os.path.exists(corresponding_source_file):
        print(f"Removing outdated documentation: {doc_file}")
        os.remove(doc_file)

# Generate New Documentation
if not source_files:
    print("No source files modified. Skipping doc generation.")
    exit(0)

for file_num, file in enumerate(source_files):
    if not os.path.exists(file):
        print(f"{file_num} ⚠️ Source file not found: {file}")
        continue

    print(f"{file_num} Generating docs for: {file}")

    documentation = new_n8n_version.get_summary(file)

    # Convert file path from /src/ to /docs/
    doc_path = "docs/ai_docs/" + file.split("/", 1)[1]

    # Change the file extension to .md
    doc_path = (
        doc_path.replace(".py", ".md")
        .replace(".gd", ".markdown")
        .replace(".cpp", ".cpp.md")
        .replace(".rs", ".rs.md")
        .replace(".c", ".c.md")
        .replace(".h", ".h.md")
    )

    # Ensure parent directories exist
    os.makedirs(os.path.dirname(doc_path), exist_ok=True)

    # Write the documentation to the mirrored docs folder
    with open(doc_path, "w") as f:
        f.write(f"# Documentation for {file}\n\n{documentation}")

    print(f"✅ Saved docs: {doc_path}")

```
