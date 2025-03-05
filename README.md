# Auto-Terminating Hello World Script

A simple Python script that displays "Hello World!" every minute and automatically terminates after 72 hours of runtime.

## Features

- Displays a message every minute
- Clears the console between messages
- Automatically terminates after 72 hours to prevent indefinite running

## Requirements

- Python 3.x

## How to Run

Simply execute the Python script:

```python
python main.py
```
## How It Works

The script uses Python's threading module to set up a timer that will terminate the program after 72 hours. It then enters an infinite loop that:

1. Prints "Hello World!" to the console
2. Waits for 60 seconds
3. Clears the console screen (works on Windows systems)

Note: If you're using a non-Windows system, you may need to replace `os.system('cls')` with `os.system('clear')`.
