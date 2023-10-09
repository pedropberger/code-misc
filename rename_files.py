##########################
# Jogando para o banco   #
##########################

import os

# Function to rename files in a directory
def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # Split the filename and extension
            root, extension = os.path.splitext(filename)
            
            # Check if the filename has at least 7 characters
            if len(root) >= 7:
                # Remove the last 7 characters from the filename
                new_root = root[:-7]
                
                # Construct the new filename by adding back the extension
                new_filename = new_root + extension
                
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f"Renamed {filename} to {new_filename}")

# Specify the path to the main folder containing subfolders
main_folder = "/CAIJ/Arquivos"

# Iterate through subfolders and rename files
for subfolder in os.listdir(main_folder):
    subfolder_path = os.path.join(main_folder, subfolder)
    if os.path.isdir(subfolder_path):
        rename_files_in_directory(subfolder_path)
