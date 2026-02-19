import os
from shutil import copy2
from time import time
from datetime import datetime

def auto_backup(dir_abs_path, db_path):
    backup_dir_path = os.path.join(dir_abs_path, 'backups')
    last_backup_path = os.path.join(backup_dir_path, '_last_backup')
    
    # Create backup directory if it doesn't exist
    if not os.path.exists(backup_dir_path):
        os.makedirs(backup_dir_path)

    # What was the last backup time?
    now = time()
    if os.path.exists(last_backup_path):
        with open(last_backup_path, 'r') as f:
            last_time = float(f.read())
    else:
        last_time = 0

    # If more than 30 days have passed since the last backup, create a new one
    if now - last_time > 2592000:
        timestamp = datetime.now().strftime("%Y-%m-%d")
        backup_path = os.path.join(backup_dir_path, f'backup_{timestamp}.json')
        
        # Backup DB
        if os.path.exists(db_path):
            copy2(db_path, backup_path)
            
            # Update last backup time
            with open(last_backup_path, 'w') as f:
                f.write(str(now))


if __name__ == "__main__":
    dir_abs_path = os.path.dirname(os.path.abspath(__file__))
    db_abs_path = os.path.join(dir_abs_path, 'listecky.json')
    auto_backup(dir_abs_path, db_abs_path)