import shutil
import os
from datetime import datetime

DB_NAME = "FinManager.db"
BACKUP_DIR = "backups"

def backup_database():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{BACKUP_DIR}/finance_backup_{timestamp}.db"

    try:
        shutil.copy(DB_NAME, backup_file)
        print(f"✅ Backup created successfully at: {backup_file}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def restore_database():
    print("\n📂 Available Backups:")
    if not os.path.exists(BACKUP_DIR):
        print("❌ No backup directory found.")
        return

    backups = os.listdir(BACKUP_DIR)
    if not backups:
        print("❌ No backup files found.")
        return

    for i, file in enumerate(backups, 1):
        print(f"{i}. {file}")

    choice = input("Select a backup number to restore: ")
    try:
        selected = backups[int(choice) - 1]
        shutil.copy(f"{BACKUP_DIR}/{selected}", DB_NAME)
        print("✅ Database restored successfully.")
    except (IndexError, ValueError):
        print("❌ Invalid selection.")
    except Exception as e:
        print(f"❌ Restore failed: {e}")
