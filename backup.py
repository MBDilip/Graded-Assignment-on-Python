import os
import shutil
import sys
from datetime import datetime

def backup_files(source, destination):
    try:
        # Check if source and destination directories exist
        if not os.path.exists(source):
            raise Exception(f"Source directory {source} does not exist.")
        if not os.path.exists(destination):
            os.makedirs(destination)

        # Iterate over all files in the source directory
        for filename in os.listdir(source):
            source_file = os.path.join(source, filename)
            destination_file = os.path.join(destination, filename)

            # Check if file already exists in destination
            if os.path.isfile(destination_file):
                # Append timestamp to filename for uniqueness
                base, extension = os.path.splitext(destination_file)
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                destination_file = f"{base}_{timestamp}{extension}"

            # Copy file from source to destination
            shutil.copy2(source_file, destination_file)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
    else:
        source_dir = sys.argv[1]
        destination_dir = sys.argv[2]
        backup_files(source_dir, destination_dir)
        print("Backup completed successfully.")
