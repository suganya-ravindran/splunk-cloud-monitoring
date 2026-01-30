import os
import time
from datetime import datetime

# --- CONFIGURATION ---
# Replace this with your Windows Instance Private IP
TARGET_IP = "172.31.21.50" 
# ---------------------

print(f"--- STARTING MONITORING FOR: {TARGET_IP} ---")

def log_to_file(message):
    # We write to a file so Splunk can read it
    with open("/home/ubuntu/server_status.log", "a") as f:
        f.write(f"{message}\n")

while True:
    # Ping the server (1 packet)
    # The > /dev/null 2>&1 part silences the ping command output in the terminal
    response = os.system(f"ping -c 1 {TARGET_IP} > /dev/null 2>&1")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if response == 0:
        msg = f"[{timestamp}] STATUS=UP Target={TARGET_IP}"
        print(msg) 
        log_to_file(msg)
    else:
        msg = f"[{timestamp}] STATUS=DOWN Target={TARGET_IP} ALERT: Critical Failure"
        print(msg)
        log_to_file(msg)
    
    # Wait 5 seconds before the next check
    time.sleep(5)
