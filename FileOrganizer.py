import os
import shutil                   # For moving files between directories
from datetime import datetime 
import time  
import logging


logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


#Define File Categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", '.tiff'],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".flv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".sh"],
    "Data": [".csv", ".json", ".xml", ".sql"],
    "Others": []        # files that don't fit into any categories   
}



'''
_______________________________________________________________________________________
                        Functions
'''

# Function to get a unique filename
def get_unique_filename(destination_path):
    """Generate a unique filename if one already exists"""
   
    base, extension = os.path.splitext(destination_path)
    counter = 1

    while os.path.exists(destination_path):
        destination_path = f"{base}_{counter}{extension}"
        counter += 1

    return destination_path


def organize_files(directory, dry_run=False):
    """Organizes files in the specified directory"""

    logging.info(f"Started organizing directory: {directory} | Dry run: {dry_run}")

    # Create folder for Category if they don't exist
    for category in FILE_CATEGORIES:
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    # Move Files into appropriate Folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        file_moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                destination = os.path.join(directory, category, filename)
                destination = get_unique_filename(destination)
                if dry_run:
                    print(f"[DRY_RUN] Move: {file_path} -> {destination}")
                    logging.info(f"[DRY_RUN] Move: {file_path} -> {destination}")
                else:
                    shutil.move(file_path, destination)
                    logging.info(f"Moved: {file_path} -> {destination}")
                file_moved = True
                break

        if not file_moved:
            destination = os.path.join(directory, "Others", filename)
            destination = get_unique_filename(destination)
            if dry_run:
                print(f"[DRY_RUN] Move: {file_path} -> {destination}")
                logging.info(f"[DRY_RUN] Move: {file_path} -> {destination}")
            else:
                shutil.move(file_path, destination)
                logging.info(f"Moved: {file_path} -> {destination}")

    if dry_run:
        print("Dry run completed. No files were moved.")
        logging.info("Dry run completed. No files were moved.")
    else:   
        print(f"Files in '{directory}' have been organized successfully.")
        logging.info(f"Files in '{directory}' have been organized successfully.")


# Scheduling the script to run at a specific time
def schedule_organizer(run_time, directory_toOrganize, dry_run=False):
    """Schedules the file organizer to run at a specific time (24-hour format)"""
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == run_time:
            organize_files(directory_toOrganize, dry_run=dry_run)
            break
        time.sleep(30) 



if __name__ == "__main__":

    while True:
        dry_run_input = input("Do you want to perform a dry run? (yes/no): ")
        if dry_run_input.lower() in ["yes", "no"]:
            dry_run = dry_run_input.lower() == "yes"
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        run_time = input("Do you want to schedule the organizer? (yes/no): ")
        if run_time.lower() == "yes":
            while True:
                try: 
                    run_time = input("Enter the time to run the organizer (24-hour format): ")
                    datetime.strptime(run_time, "%H:%M")  # Validate time format    
                    
                    directory= input("Enter the directory path to organize: ")
                    if not os.path.isdir(directory):
                        print(f"Error: '{directory}' is not a valid directory.")
                        logging.error(f"Invalid directory: {directory}")
                        continue
                    
                    schedule_organizer(run_time, directory, dry_run)
                    break

                except ValueError:
                    print("Invalid time format. Please use 24-hour format (HH:MM).")
                    logging.error(f"Invalid time format: {run_time}")
            
        elif run_time.lower() == "no":
            directory_toOrganize = input("Enter the directory path to organize: ")
            organize_files(directory_toOrganize, dry_run)

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")