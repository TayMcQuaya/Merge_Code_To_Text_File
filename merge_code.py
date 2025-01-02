import os

def merge_files():
    # Define common programming file types (excluding .json by default)
    file_types = [
        "py", "html", "css", "cpp", "c", "java", "rb", "php", "ts","js",
        "go", "swift", "kt", "rs", "sh", "bat", "cs", "xml", "yaml", "toml", "ini", "tsx", "mjs"
    ]

    # Get the root directory (current working directory)
    root_dir = os.getcwd()

    # Output file name
    output_file_name = "merged_files.txt"
    output_file_path = os.path.join(root_dir, output_file_name)

    # Define directories and files to ignore
    ignore_dirs = {"node_modules", "venv", ".git", "__pycache__", "dist", "build", "deps", "dependencies", "vendor"}
    ignore_file_patterns = {
        ".lock", ".pyc", ".pyo", ".min.js", ".map", 
        "merge_code.py", "merged_files.txt", "project_structure.py", "gitauto.py"
    }

    # Special cases for exceptions
    include_specific_files = {"package.json"}  # Only include package.json, exclude package-lock.json

    # Find all files with the specified extensions
    files_to_merge = []
    for root, dirs, files in os.walk(root_dir):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs and not any(dep in d.lower() for dep in ignore_dirs)]

        for file in files:
            file_path = os.path.join(root, file)

            # Include specific files (e.g., package.json only)
            if file in include_specific_files:
                files_to_merge.append(file_path)
                continue

            # Exclude explicitly ignored filenames
            if file in {"project_structure.py", "gitauto.py"}:
                continue

            # Check for other file types, excluding all .json files except the specific ones above
            if any(file.endswith(f".{ext}") for ext in file_types) and not file.endswith(".json"):
                if not any(file.endswith(ignored) for ignored in ignore_file_patterns):
                    files_to_merge.append(file_path)

    # If no matching files found, exit the function
    if not files_to_merge:
        print(f"No files with the specified types ({', '.join(file_types)}) found in {root_dir}.")
        return

    # Merge files into the output file (overwrite if it already exists)
    with open(output_file_path, "w", encoding="utf-8") as outfile:
        for file_path in files_to_merge:
            file_name = os.path.basename(file_path)
            outfile.write(f"# {'='*80}\n")
            outfile.write(f"# File: {file_name}\n")
            outfile.write(f"# {'='*80}\n\n")
            with open(file_path, "r", encoding="utf-8") as infile:
                try:
                    outfile.write(infile.read())
                except UnicodeDecodeError:
                    print(f"Skipping binary or unreadable file: {file_path}")
                outfile.write("\n\n")

    print(f"Merged files saved to: {output_file_path}")

    # Add merge_code.py and merged_files.txt to .gitignore
    gitignore_path = os.path.join(root_dir, ".gitignore")
    try:
        if os.path.exists(gitignore_path):
            with open(gitignore_path, "r", encoding="utf-8") as gitignore:
                gitignore_content = gitignore.read()
            added_entries = []
            for file_to_ignore in ["merge_code.py", "merged_files.txt"]:
                if file_to_ignore not in gitignore_content:
                    added_entries.append(file_to_ignore)
            if added_entries:
                with open(gitignore_path, "a", encoding="utf-8") as gitignore:
                    gitignore.write("\n" + "\n".join(added_entries) + "\n")
                print(f"Added {', '.join(added_entries)} to existing .gitignore.")
            else:
                print("merge_code.py and merged_files.txt are already in .gitignore.")
        else:
            with open(gitignore_path, "w", encoding="utf-8") as gitignore:
                gitignore.write("merge_code.py\nmerged_files.txt\n")
            print("Created a new .gitignore and added merge_code.py and merged_files.txt.")
    except Exception as e:
        print(f"Error handling .gitignore: {e}")

if __name__ == "__main__":
    merge_files()
