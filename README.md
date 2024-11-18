# Merge Code Script

This script merges files of specific types (like `.py`, `.js`, etc.) from the current directory and its subdirectories into a single text file. It is designed to make it easy to gather code or text from multiple files in a project into one place.

## What the Script Does

1. **Prompts for File Types**:
   - You can specify one or more file types (e.g., `py` for Python files or `js` for JavaScript files).
   - If you type `web`, the script will automatically include `html`, `css`, and `js` files for merging.

2. **Scans Your Directory**:
   - The script looks through the current directory and all subdirectories for files matching the types you specify.

3. **Creates a Merged File**:
   - It combines the contents of all matching files into a new file called `merged_files.txt`.
   - Each file's contents in the merged file are clearly labeled with its original file name.

4. **Handles Dependency Files**:
   - The script skips common dependency files and directories, such as `node_modules`, `venv`, `.git`, and others.

5. **Updates `.gitignore`**:
   - Ensures that both the script (`merge_code.py`) and the merged output file (`merged_files.txt`) are added to `.gitignore` so they are not accidentally committed to version control.

## How to Use the Script

1. **Run the Script**:
   ```bash
   python merge_code.py
   ```

2. **Enter File Types**:
   - When prompted, type the file type you want to include (e.g., `py` for Python files).
   - To include `html`, `css`, and `js` files, simply type `web`.
   - The script will ask if you want to include additional file types. Type another file type (e.g., `txt`) or `no` to finish.

3. **View the Merged File**:
   - After the script runs, a file named `merged_files.txt` will appear in the root directory.
   - Open this file to see the contents of all the merged files, labeled by their original file names.

## Example Interaction

```bash
Enter the file type (e.g., 'py' for Python files or 'web' for HTML/CSS/JS): web
Do you want any other file types to be included? Type the file type or 'no': py
Do you want any other file types to be included? Type the file type or 'no': no
Merged files saved to: /path/to/your/directory/merged_files.txt
Added merge_code.py, merged_files.txt to existing .gitignore.
```

## Notes

- If no files of the specified types are found, the script will notify you and exit without creating a merged file.
- If a `.gitignore` file already exists, the script will add `merge_code.py` and `merged_files.txt` to it (if not already present). If `.gitignore` does not exist, the script will create one.

## Requirements

- Python 3.x
- No additional libraries are required.

## Troubleshooting

- Ensure the script is placed in the directory where you want to scan for files.
- If the merged file is not created, check the file types you entered and ensure matching files exist in your directory.

## License

Feel free to use and modify this script as needed.

