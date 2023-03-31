import random
import time
import threading

# Define parameters
disaster_prob = 0.01
recovery_time = 5
monitoring_interval = 1

# Define global variables
failed = False
recovery_start_time = 0

# Define function to simulate system failure and recovery
def simulate_disaster():
    global failed
    global recovery_start_time
    while True:
        # Simulate system failure
        if random.random() < disaster_prob and not failed:
            print("System failure detected!")
            failed = True
            recovery_start_time = time.time()
        # Simulate system recovery
        if failed and time.time() - recovery_start_time > recovery_time:
            print("System recovered!")
            failed = False
        time.sleep(0.1)

# Define function to monitor system status and trigger recovery
def monitor_system():
    global failed
    while True:
        # Monitor system status
        if not failed:
            print("System operating normally.")
        # Trigger recovery
        else:
            print("Triggering disaster recovery...")
            time.sleep(3)
            print("Disaster recovery complete.")
        time.sleep(monitoring_interval)

# Start simulation threads
disaster_thread = threading.Thread(target=simulate_disaster)
monitor_thread = threading.Thread(target=monitor_system)
disaster_thread.start()
monitor_thread.start()
