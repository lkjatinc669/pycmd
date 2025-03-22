# PyCmd - Custom Command Shell

## Overview
PyCmd is a simple Python-based command shell that allows users to execute system commands, rename the shell prompt, and log command outputs to a file (`stdout.txt`).

## Features
- Executes system commands via `subprocess.run()`
- Logs command output and errors with timestamps
- Allows renaming the shell prompt using `set name=<new_name>`
- Handles exit commands (`exit`, `quit`)

## Requirements
- Python 3.x

## Installation
No installation is required. Simply download the script and run it.

## Usage
Run the script using:
```bash
python script.py
```

### Commands:
- **Executing System Commands**: Enter any valid command supported by your operating system.
- **Renaming the Shell Prompt**:
  ```bash
  set name=<new_prompt_name>
  ```
- **Exiting the Shell**:
  ```bash
  exit
  ```
  or
  ```bash
  quit
  ```

## Logging
- All command outputs (both stdout and stderr) are saved in `stdout.txt` with timestamps.

## Error Handling
- If an invalid `set name` command is used, an error message is displayed.
- The script handles `KeyboardInterrupt` gracefully.

## License
This project is open-source and free to use.

## Author
[Jatin Gohil](https://github.com/lkjatinc669)  
[lkjgclabs]
