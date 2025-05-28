# 🕐 Shutdown Timer Template

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/Esqyzan/Shutdown-timer)](https://github.com/Esqyzan/Shutdown-timer/stargazers)

**A universal template for creating Python programs with automatic shutdown after a specified time.**

This project serves as a ready-to-use code template that can be used as a foundation for any programs requiring automatic termination. Perfect for long-running tasks, monitoring, automation, and other scenarios where you need to prevent infinite execution.

## 🎯 Template Purpose

This code serves as a **base template** for developing programs with auto-shutdown functionality:

- 📋 **Ready-to-use foundation** for your timer-based projects
- 🔧 **Easily adaptable** code for any tasks
- 🛡️ **Reliable system** for preventing program hanging
- 📚 **Educational example** of threading in Python

## 🌟 Template Features

- ⏰ **Threading-based Timer**: Automatic termination after specified time
- 🔄 **Cyclic Execution**: Foundation for repetitive tasks
- 🧹 **Console Clearing**: Clean output between iterations
- 🛡️ **Hang Protection**: Guaranteed program termination
- 🔧 **Daemon Threading**: Reliable background process shutdown

## 📋 Requirements

- Python 3.x
- Operating System: Windows, Linux, macOS

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/Esqyzan/Shutdown-timer.git
cd Shutdown-timer
```

2. Run the basic example:
```bash
python main.py
```

3. Adapt the code for your tasks!

## 🛠️ How to Use This Template

### Core Code Structure:

```python
def setup_shutdown_timer(timeout_seconds):
    """Setup automatic program termination"""
    def force_exit():
        print(f"\nTime's up! The program will be forcibly terminated.")
        os._exit(0)
    
    timer = threading.Timer(timeout_seconds, force_exit)
    timer.daemon = True  # Daemon thread for clean shutdown
    timer.start()

# Your main code here
def main_logic():
    # Replace this block with your logic
    while True:
        # Your task execution code
        print("Executing your task...")
        time.sleep(60)  # Interval between executions
```

### Adaptation Examples:

**For System Monitoring:**
```python
def monitor_system():
    while True:
        # Check system status
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        log_metrics(cpu_usage, memory_usage)
        time.sleep(300)  # Check every 5 minutes
```

**For Data Processing:**
```python
def process_data():
    while True:
        # Process new files
        files = get_new_files()
        for file in files:
            process_file(file)
        time.sleep(3600)  # Check every hour
```

**For Web Scraping:**
```python
def scrape_websites():
    while True:
        # Scrape target websites
        for url in target_urls:
            data = scrape_website(url)
            save_to_database(data)
        time.sleep(1800)  # Scrape every 30 minutes
```

## ⚙️ Timer Configuration

Modify the auto-termination time in line 15 of `main.py`:

```python
setup_shutdown_timer(259200)  # 72 hours in seconds
```

### Common Timer Values:
- **1 hour**: `3600`
- **6 hours**: `21600`  
- **24 hours**: `86400`
- **48 hours**: `172800`
- **72 hours**: `259200` (default)
- **1 week**: `604800`

## 🖥️ Cross-Platform Compatibility

- **Windows**: Uses `os.system('cls')` for screen clearing
- **Linux/macOS**: Replace `os.system('cls')` with `os.system('clear')` on line 22

## 💡 Use Cases

This template is perfect for:

- 🔍 **System and server monitoring**
- 📊 **Background data collection and processing**
- 🤖 **Task automation** with time limits
- 🧪 **Long-running tests** and experiments
- 📈 **Data parsing and analysis** of large datasets
- 🔄 **Periodic cache or database updates**
- 🌐 **Web scraping** with scheduled intervals
- 📧 **Automated reporting** and notifications
- 🔄 **Backup processes** with time constraints
- 🎯 **Performance benchmarking** over time

## 🧵 Threading Implementation Details

The template demonstrates key threading concepts:

- **Timer Thread**: Separate thread handles automatic termination
- **Main Thread**: Handles the primary program logic
- **Daemon Mode**: Ensures timer thread terminates with program exit
- **Thread Safety**: Uses `os._exit(0)` for guaranteed termination

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

## 🔧 Customization Tips

### Adding Logging:
```python
import logging

logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(message)s')

def your_task():
    logging.info("Task started")
    # Your code here
    logging.info("Task completed")
```

### Adding Configuration File:
```python
import json

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

config = load_config()
timeout = config.get('timeout_hours', 72) * 3600
```

### Adding Signal Handling:
```python
import signal
import sys

def signal_handler(sig, frame):
    print('\nGraceful shutdown initiated...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
```

## 🤝 Contributing

Improvements to the template are welcome:
- Adding new usage examples
- Improving cross-platform compatibility
- Performance optimizations
- Documentation and examples

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐ Star this repository if this template was useful for your projects!

**💡 Tip**: Use this code as a foundation for your projects requiring automatic termination!
