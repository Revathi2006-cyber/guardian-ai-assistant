# logger.py

from datetime import datetime

def log_emergency(command, location_url):
    try:
        with open("emergency_logs.txt", "a") as f:
            f.write(f"Time: {datetime.now()}\n")
            f.write(f"Voice Command: {command}\n")
            f.write(f"Location: {location_url}\n")
            f.write("-" * 40 + "\n")
    except Exception as e:
        print(f"Logging failed: {e}")