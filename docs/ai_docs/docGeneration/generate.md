# Documentation for src/docGeneration/generate.py

# AI Summary
This script automates the process of generating and maintaining documentation for source files in a project. It retrieves the list of modified files, filters the source files, removes outdated documentation, and generates new documentation using the new_n8n_version.get_summary function. The script ensures that the documentation is saved in the correct directory with the appropriate file extensions.

The AI gave it a general rating of 8/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is well-structured and follows good practices. It uses meaningful variable names and includes comments to explain the purpose of each section. The code is also well-organized and easy to follow. However, there is room for improvement in terms of error handling and input validation.
# Functions

## get_modified_files
### Explanation
This function retrieves a list of files that have been modified in the last commit. It uses the git diff command to get the names of the modified files and returns them as a list.
### Code
```python
git_diff_cmd = "git diff --name-only HEAD~1 HEAD"
modified_files = subprocess.check_output(git_diff_cmd.split()).decode().splitlines()

print("Modified files:", modified_files)
```

## filter_source_files
### Explanation
This function filters the list of modified files to include only those files that are located in the /src/ directory and have a file extension of .py, .gd, .cpp, .rs, .c, or .h. It returns the filtered list of source files.
### Code
```python
source_files = [
    f
    for f in modified_files
    if f.startswith("src/") and f.endswith((".py", ".gd", ".cpp", ".rs", ".c", ".h"))
]

print(f"{len(source_files)}; Source files:", source_files)
```

## get_documentation_files
### Explanation
This function retrieves a list of documentation files located in the docs/ai_docs/ directory. It uses the os.walk function to traverse the directory tree and collect the file paths.
### Code
```python
documentation_files = [
    os.path.join(dirpath, f)
    for (dirpath, dirnames, filenames) in os.walk("docs/ai_docs/")
    for f in filenames
]
print(f"{len(documentation_files)}; Documentation files:", documentation_files)
```

## remove_outdated_documentation
### Explanation
This function removes outdated documentation files that correspond to source files that have been deleted. It iterates through the list of documentation files, checks if the corresponding source file exists, and removes the documentation file if the source file does not exist.
### Code
```python
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
This function generates new documentation for modified source files. It iterates through the list of source files, generates documentation using the new_n8n_version.get_summary function, and writes the documentation to the corresponding markdown file in the docs/ai_docs/ directory. It also ensures that the parent directories exist before writing the documentation.
### Code
```python
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

## main
### Explanation
This is the main function that orchestrates the documentation generation process. It calls the other functions in sequence to get the list of modified files, filter the source files, get the list of documentation files, remove outdated documentation, and generate new documentation. It also handles the case where no source files are modified.
### Code
```python
if not source_files:
    print("No source files modified. Skipping doc generation.")
    exit(0)
```
# Overall File Contents
```python
import os
import subprocess
import new_n8n_version

# Get list of modified files in the last commit
git_diff_cmd = "git diff --name-only HEAD~1 HEAD"
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
