import psutil
import logging
import time


logging.basicConfig(filename="system_health.log",
                    level=logging.WARNING,
                    format="%(asctime)s - %(levelname)s - %(message)s")


CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80  
DISK_THRESHOLD = 90  
PROCESS_THRESHOLD = 200  

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    process_count = len(psutil.pids())

    if cpu_usage > CPU_THRESHOLD:
        alert = f" High CPU Usage: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)"
        logging.warning(alert)
        print(alert)

    if memory_usage > MEMORY_THRESHOLD:
        alert = f" High Memory Usage: {memory_usage}% (Threshold: {MEMORY_THRESHOLD}%)"
        logging.warning(alert)
        print(alert)

    if disk_usage > DISK_THRESHOLD:
        alert = f" High Disk Usage: {disk_usage}% (Threshold: {DISK_THRESHOLD}%)"
        logging.warning(alert)
        print(alert)

    if process_count > PROCESS_THRESHOLD:
        alert = f" High Process Count: {process_count} (Threshold: {PROCESS_THRESHOLD})"
        logging.warning(alert)
        print(alert)

    # Print current system status
    print(f" CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%, Processes: {process_count}")

if __name__ == "__main__":
    while True:
        check_system_health()
        time.sleep(10)  # Check every 10 seconds

