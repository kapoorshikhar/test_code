import os
import shutil

# List of files to delete
files_to_delete = ['descriptions.txt', 'titles.txt', 'image_urls.txt']

for file_path in files_to_delete:
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been successfully deleted")
    except FileNotFoundError:
        print(f"File '{file_path}' does not exist")
    except Exception as e:
        print(f"Error deleting file '{file_path}': {e}")

# List of folders to delete
folders_to_delete = ['images']

for folder_path in folders_to_delete:
    try:
        shutil.rmtree(folder_path)  # Deletes folder and contents
        print(f"Folder '{folder_path}' and its contents have been successfully deleted")
    except FileNotFoundError:
        print(f"Folder '{folder_path}' does not exist")
    except Exception as e:
        print(f"Error deleting folder '{folder_path}': {e}")
