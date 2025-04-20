import os 
import shutil

import tkinter.messagebox

def Run(params):

    if params["recursive_filter"] == 1:
        warningContent = "Recursive filtering enabled, only use this on controlled folders, as every subfolder will be cleaned. Do you want to continue?"
        if tkinter.messagebox.askquestion("Recursive Filter", warningContent) == "no":
            return

        ##if no, return

    #change this to radio buttons as needed
    if params["dir"] != "" and params["type_filter"] == "type":
        sort_files_by_extension(params["dir"])

    if params["dir"] != "" and params["type_filter"] == "size":
        sort_files_by_size(params["dir"])

    if params["dir"] != "" and params["empty_filter"] == 1:
        remove_empty_folders(params["dir"])
        
def sort_files_by_extension(directory):
    # Check if the given directory exists
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        # Get the file extension (without the dot)
        file_extension = os.path.splitext(file)[1][1:].lower()

        if file_extension:
            # Create a folder for the extension if it doesn't exist
            extension_folder = os.path.join(directory, file_extension)
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            # Define source and destination paths
            source = os.path.join(directory, file)
            destination = os.path.join(extension_folder, file)

            # Move the file to the appropriate folder
            shutil.move(source, destination)
            print(f"Moved: {file} -> {extension_folder}")
        else:
            print(f"Skipping file (no extension): {file}")


def sort_files_by_size(directory):
    # Check if the given directory exists
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        # Get the file's full path
        file_path = os.path.join(directory, file)

        # Get the file size in bytes
        file_size = os.path.getsize(file_path)

        # Calculate the size range folder name (in increments of 300MB)
        size_range = (file_size // (300 * 1024 * 1024)) * 300  # Round down to nearest 300MB increment
        folder_name = f"{size_range}MB_to_{size_range + 300}MB"

        # Create the folder if it doesn't exist
        size_folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(size_folder_path):
            os.makedirs(size_folder_path)

        # Define the destination path
        destination = os.path.join(size_folder_path, file)

        # Move the file to the appropriate folder
        shutil.move(file_path, destination)
        print(f"Moved: {file} -> {folder_name}")


def remove_empty_folders(directory):
    # Check if the given directory exists
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    # Walk through the directory from bottom to top (reverse order)
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            # Check if the directory is empty
            if not os.listdir(dir_path):
                # Remove the empty directory
                os.rmdir(dir_path)
                print(f"Removed empty folder: {dir_path}")