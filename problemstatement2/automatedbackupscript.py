import os
import tarfile
import subprocess
import logging
import datetime

logging.basicConfig(filename="backup.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

SOURCE_DIR = "/home/user/documents"  
BACKUP_DIR = "/home/user/backups" 
REMOTE_SERVER = "user@remote-server.com"  
REMOTE_PATH = "/home/user/remote_backups"
USE_CLOUD = False  

def create_backup():
    """Create a compressed backup of the specified directory."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"backup_{timestamp}.tar.gz"
    backup_filepath = os.path.join(BACKUP_DIR, backup_filename)

   
    os.makedirs(BACKUP_DIR, exist_ok=True)

    try:
        with tarfile.open(backup_filepath, "w:gz") as tar:
            tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))
        logging.info(f"Backup created successfully: {backup_filepath}")
        return backup_filepath
    except Exception as e:
        logging.error(f"Backup creation failed: {e}")
        return None

def transfer_to_remote(backup_filepath):
    """Transfer the backup file to a remote server using SCP."""
    try:
        cmd = f"scp {backup_filepath} {REMOTE_SERVER}:{REMOTE_PATH}"
        subprocess.run(cmd, shell=True, check=True)
        logging.info(f"Backup successfully transferred to {REMOTE_SERVER}:{REMOTE_PATH}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Remote transfer failed: {e}")

def upload_to_cloud(backup_filepath):
    """Upload the backup file to Google Drive using Rclone."""
    try:
        cmd = f"rclone copy {backup_filepath} remote:BackupFolder"
        subprocess.run(cmd, shell=True, check=True)
        logging.info("Backup successfully uploaded to Google Drive")
    except subprocess.CalledProcessError as e:
        logging.error(f"Cloud upload failed: {e}")

if __name__ == "__main__":
    backup_file = create_backup()
    if backup_file:
        transfer_to_remote(backup_file)  # Send to remote server
        if USE_CLOUD:
            upload_to_cloud(backup_file)  # Upload to Google Drive (if enabled)
    else:
        logging.error("Backup process failed. No file to transfer.")

