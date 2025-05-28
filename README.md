# 🕐 Shutdown Timer

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/Esqyzan/Shutdown-timer)](https://github.com/Esqyzan/Shutdown-timer/stargazers)

A simple Python script that displays messages every minute and automatically terminates after a specified time period (default: 72 hours) using threading-based timer functionality.

## 🌟 Features

- ⏰ **Threading-based Timer**: Automatic termination after 72 hours using `threading.Timer`
- 🔄 **Periodic Output**: Displays message every minute
- 🧹 **Console Clearing**: Clears screen between messages for clean output
- 🛡️ **Fail-safe Mechanism**: Prevents infinite execution
- 🔧 **Daemon Threading**: Uses daemon threads for reliable shutdown

## 📋 Requirements

- Python 3.x
- Operating System: Windows, Linux, macOS

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/Esqyzan/Shutdown-timer.git
cd Shutdown-timer
```

2. Run the script:
```bash
python main.py
```

## ⚙️ How It Works

The core functionality revolves around Python's **threading module** to create a reliable auto-termination system:

### Threading Implementation:

```python
def setup_shutdown_timer(timeout_seconds):
    def force_exit():
        print(f"\nTime's up! The program will be forcibly terminated.")
        os._exit(0)
    
    timer = threading.Timer(timeout_seconds, force_exit)
    timer.daemon = True  # Daemon thread ensures clean shutdown
    timer.start()
```

### Process Flow:

1. **Timer Setup**: Creates a `threading.Timer` object with 72-hour timeout
2. **Daemon Thread**: Sets timer as daemon to ensure proper cleanup
3. **Main Loop**: Executes display cycle every 60 seconds
4. **Force Exit**: Timer automatically calls `os._exit(0)` when timeout reached

## 🔧 Configuration

Modify the timeout by changing line 15 in `main.py`:

```python
setup_shutdown_timer(259200)  # 72 hours in seconds
```

### Common Timer Values:
- **1 hour**: `3600`
- **6 hours**: `21600`  
- **24 hours**: `86400`
- **48 hours**: `172800`
- **72 hours**: `259200` (default)

## 🖥️ Cross-Platform Compatibility

- **Windows**: Uses `os.system('cls')` for screen clearing
- **Linux/macOS**: Replace `os.system('cls')` with `os.system('clear')` on line 22

## 📝 Example Output

```bash
$ python main.py
The program will end automatically after 72 hours.
Hello World!
# (60-second pause, then screen clear)
Hello World!
# (continues for 72 hours)
Time's up! The program will be forcibly terminated.
```

## 🧵 Threading Details

The script demonstrates key threading concepts:

- **Timer Thread**: Separate thread handles automatic termination
- **Main Thread**: Handles the display loop
- **Daemon Mode**: Ensures timer thread doesn't prevent program exit
- **Thread Safety**: Uses `os._exit(0)` for guaranteed termination

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐ Star this repository if you found it useful!
