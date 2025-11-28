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
    if f.startswith("src/") and f.endswith((".py", ".gd", ".cpp", ".rs", '.c', '.h'))
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
