# Documentation for src/docGeneration/generate.py

# Python Script Documentation

## Program Overview

The provided Python script is designed to automate the generation and management of documentation for modified source files. It identifies files that have been changed in the last commit, filters them based on their file type (Python, C++, or JavaScript), and then uses an OpenAI model to generate documentation for these files. The generated documentation is saved in a mirrored directory structure under `docs/ai_docs/`.

## Table of Contents

- [Configuration](#configuration)
- [Modified Files Identification](#modified-files-identification)
- [Source Files Filtering](#source-files-filtering)
- [Documentation Files Management](#documentation-files-management)
- [Documentation Generation](#documentation-generation)
- [Example Usage](#example-usage)

## Configuration

The script starts with several configuration variables:

- `CUSTOM_API_URL`: The custom API endpoint for the OpenAI service.
- `OPENAI_API_KEY`: The API key for the OpenAI service, retrieved from the environment variable `API_KEY`.
- `MODEL_NAME`: The name of the model to be used for documentation generation.

```python
CUSTOM_API_URL = "http://192.168.86.4:4001"
OPENAI_API_KEY = os.getenv("API_KEY")
MODEL_NAME = "codestral-latest"
```

## Modified Files Identification

The script uses the `git diff` command to identify files that have been modified in the last commit.

```python
git_diff_cmd = "git diff --name-only HEAD~1"
modified_files = subprocess.check_output(git_diff_cmd.split()).decode().splitlines()
print("Modified files:", modified_files)
```

## Source Files Filtering

The script filters the modified files to include only those located in the `src/` directory and with extensions `.py`, `.cpp`, or `.js`.

```python
source_files = [f for f in modified_files if f.startswith("src/") and f.endswith((".py", ".cpp", ".js"))]
print(f"{len(source_files)}; Source files:", source_files)
```

## Documentation Files Management

The script identifies existing documentation files in the `docs/ai_docs/` directory and removes any documentation files that correspond to source files that no longer exist.

```python
documentation_files = [os.path.join(dirpath, f) for (dirpath, dirnames, filenames) in os.walk('docs/ai_docs/') for f in filenames]
print(f"{len(documentation_files)}; Documentation files:", documentation_files)

for doc_file in documentation_files:
    corresponding_source_file = doc_file.replace("docs/ai_docs/", "src/").replace(".md", ".py")
    if not os.path.exists(corresponding_source_file):
        print(f"Removing outdated documentation: {doc_file}")
        os.remove(doc_file)
```

## Documentation Generation

The script initializes an OpenAI client with the custom API URL and API key. For each source file, it reads the file's content, sends it to the OpenAI model for documentation generation, and saves the generated documentation in the `docs/ai_docs/` directory.

```python
if not source_files:
    print("No source files modified. Skipping doc generation.")
    exit(0)

client = openai.OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=CUSTOM_API_URL
)

for file_num, file in enumerate(source_files):
    if not os.path.exists(file):
        print(f"{file_num} ⚠️ Source file not found: {file}")
        continue

    print(f"{file_num} Generating docs for: {file}")
    with open(file, "r") as f:
        code = f.read()

    prompt = load_from_file("src/docGeneration/prompt.md")

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": code}
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.7,
        max_tokens=1000
    )

    documentation = response.choices[0].message.content

    if not documentation:
        print(f"⚠️ No documentation generated for {file}")
        continue

    doc_path = file.replace("src/", "docs/ai_docs/").replace(".py", ".md").replace(".cpp", ".md").replace(".js", ".md")
    os.makedirs(os.path.dirname(doc_path), exist_ok=True)

    with open(doc_path, "w") as f:
        f.write(f"# Documentation for {file}\n\n{documentation}")

    print(f"✅ Saved docs: {doc_path}")
```

