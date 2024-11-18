# Merge Files Script

## Overview

This script automatically scans your project directory for commonly known programming files (e.g., `.py`, `.html`, `.css`, `.js`, `.cpp`, and others) and merges their contents into a single file called `merged_files.txt`. It also ensures that the script itself and its output file are ignored in version control by adding them to `.gitignore`.

### Key Features:
- Scans the current working directory recursively.
- Ignores common dependency directories (e.g., `node_modules`, `venv`, `.git`).
- Handles various file types including Python, HTML, CSS, JavaScript, C++, and more.
- Merges content into `merged_files.txt` with file headers for easy identification.
- Automatically updates or creates a `.gitignore` file to exclude `merge_code.py` and `merged_files.txt`.
- Skips binary or unreadable files gracefully.

## How to Run

1. Clone or download the script to your project directory.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:

   ```bash
   python merge_code.py
   ```

4. The script will:
   - Scan all subdirectories for supported file types.
   - Merge their content into a single file named `merged_files.txt` in the current directory.
   - Skip any ignored directories and files.

5. Check the output file `merged_files.txt` in the project root for the merged content.

## Supported File Types

The script automatically detects and processes the following file types:

- Python (`.py`)
- HTML (`.html`)
- CSS (`.css`)
- JavaScript (`.js`)
- C++ (`.cpp`), C (`.c`)
- Java (`.java`)
- Ruby (`.rb`)
- PHP (`.php`)
- TypeScript (`.ts`)
- Go (`.go`)
- Swift (`.swift`)
- Kotlin (`.kt`)
- Rust (`.rs`)
- Shell scripts (`.sh`, `.bat`)
- C# (`.cs`)
- XML (`.xml`)
- JSON (`.json`)
- YAML (`.yaml`)
- TOML (`.toml`)
- INI (`.ini`)

## Directory and File Exclusions

The script skips the following:

### Ignored Directories:
- `node_modules`
- `venv`
- `.git`
- `__pycache__`
- `dist`
- `build`

### Ignored File Patterns:
- `.lock`
- `.pyc`, `.pyo`
- `.min.js`
- `.map`
- `merge_code.py`
- `merged_files.txt`

## Notes

- If no files matching the supported types are found, the script will notify you and terminate without creating the output file.
- If `.gitignore` exists, the script checks and appends `merge_code.py` and `merged_files.txt` if they are not already listed. If `.gitignore` is missing, the script creates one.
- Binary or unreadable files are skipped with a warning in the terminal.

## Troubleshooting

- **Skipped Files:** If a file is skipped as unreadable, check its encoding or ensure it’s not a binary file.
- **No Output:** Verify that the directory contains files of the supported types and is not empty.

## License

This script is free to use and modify for any personal or commercial project.

