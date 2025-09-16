import shutil
import os

def copy_files(file_list, src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    for filename in file_list:
        src_path = os.path.join(src_folder, filename)
        dest_path = os.path.join(dest_folder, filename)
        shutil.copy2(src_path, dest_path)
        print(f"Copied {src_path} to {dest_path}")
        os.remove(src_path)
        print(f"Removed {src_path} from source folder")

# Example usage:
files_to_copy = ['1.txt']
source_folder = 'D:/projects/temp'
destination_folder = 'D:/projects/temp1'

copy_files(files_to_copy, source_folder, destination_folder)