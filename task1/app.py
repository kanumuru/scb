import os

def search_string_in_files(folder_path, search_string):
    file_names = []

    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Check if the path is a file (not a directory)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Read the file content and check if the search string is present
                    file_content = file.read()
                    if search_string in file_content:
                        file_names.append(file_name)
            except Exception as e:
                print(f"Error reading file '{file_path}': {str(e)}")

    return file_names

# Example usage:
folder_path = '/Users/kanumururajesh/Desktop/tmp/scb/automation/task1'
search_string = input("Enter the search string: ")

result = search_string_in_files(folder_path, search_string)

if result:
    print(f"The search string '{search_string}' is present in the following files:")
    for file_name in result:
        print(file_name)
else:
    print(f"The search string '{search_string}' is not present in any files.")
