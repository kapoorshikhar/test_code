import os
import shutil
files_to_delete = ['4_descriptions.txt', '2_titles.txt', '3_image_urls.txt']  # Add your files here

for file_path in files_to_delete:
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been successfully deleted")
    except FileNotFoundError:
        print(f"File '{file_path}' does not exist")
    except PermissionError:
        print(f"Permission denied: Unable to delete '{file_path}'")


folders_to_delete = ['bg_img']  # Add your folders here

for folder_path in folders_to_delete:
    try:
        os.rmdir(folder_path)
        print(f"Folder '{folder_path}' has been successfully deleted")
    except FileNotFoundError:
        print(f"Folder '{folder_path}' does not exist")
    except OSError as e:
        print(f"Error deleting folder '{folder_path}': {e}")

        for folder_path in folders_to_delete:
            try:
                shutil.rmtree(folder_path)
                print(f"Folder '{folder_path}' and its contents have been successfully deleted")
            except FileNotFoundError:
                print(f"Folder '{folder_path}' does not exist")
            except PermissionError:
                print(f"Permission denied: Unable to delete '{folder_path}'")