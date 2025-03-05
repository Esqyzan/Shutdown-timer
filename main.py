import threading
import os
import time

def setup_shutdown_timer(timeout_seconds):
    def force_exit():
        print(f"\nTime's up! The program will be forcibly terminated.")
        os._exit(0)
    
    timer = threading.Timer(timeout_seconds, force_exit)
    timer.daemon = True
    timer.start()

if __name__ == "__main__":
    setup_shutdown_timer(259200)  # 72 hours in seconds
    
    print(f"The program will end automatically after 72 hours.")
    
    while True:
        print("Hello World!")
        time.sleep(60)
        os.system('cls')