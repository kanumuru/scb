import os

def search_string_in_files(folder_path, search_string):
    file_names = []

    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    # Recursively iterate through all files in the folder and its subfolders
    for folder_name, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(folder_name, file_name)

            # Check if the path is a file (not a directory)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        # Read the file content and check if the search string is present
                        file_content = file.read()
                        if search_string in file_content:
                            file_names.append(file_path)
                except Exception as e:
                    print(f"Error reading file '{file_path}': {str(e)}")

    return file_names

# Example usage:
# Example usage:
folder_path = '/Users/kanumururajesh/Desktop/tmp/scb/automation/task2'
# folder_path = input("Enter the folder path: ")
search_string = input("Enter the search string: ")

result = search_string_in_files(folder_path, search_string)

if result:
    print(f"The search string '{search_string}' is present in the following files:")
    for file_path in result:
        print(file_path)
else:
    print(f"The search string '{search_string}' is not present in any files.")
