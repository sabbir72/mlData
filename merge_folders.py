## This folder merges the "images" and "labels|" annotated folders into one single directory for splitting into "train" and "test". "valid" folders 

import os
import argparse
from tqdm import tqdm
import shutil

def merge_common_folders(source_directory, destination_directory):
    # Create destination folders if they don't exist
    os.makedirs(os.path.join(destination_directory, "images"), exist_ok=True)
    os.makedirs(os.path.join(destination_directory, "labels"), exist_ok=True)

    # List all subdirectories in the source directory
    source_folders = [os.path.join(source_directory, folder) for folder in os.listdir(source_directory) if os.path.isdir(os.path.join(source_directory, folder))]

    # Iterate over each source folder
    for source_folder in tqdm(source_folders):
        # Check if 'images' folder exists in the source folder
        if os.path.exists(os.path.join(source_folder, "images")):
            # Copy image files
            for file in tqdm(os.listdir(os.path.join(source_folder, "images"))):
                source_file_path = os.path.join(source_folder, "images", file)
                destination_file_path = os.path.join(destination_directory, "images", file)
                shutil.copy(source_file_path, destination_file_path)

        # Check if 'labels' folder exists in the source folder
        if os.path.exists(os.path.join(source_folder, "labels")):
            # Copy label files
            for file in tqdm(os.listdir(os.path.join(source_folder, "labels"))):
                source_file_path = os.path.join(source_folder, "labels", file)
                destination_file_path = os.path.join(destination_directory, "labels", file)
                shutil.copy(source_file_path, destination_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge common folders 'images' and 'labels' from a list of folders into a single destination folder.")
    parser.add_argument("--src", required=True, help="Source directory containing subdirectories with common folders 'images' and 'labels'.")
    parser.add_argument("--dst", required=True, help="Destination directory for merged 'images' and 'labels' folders.")
    args = parser.parse_args()

    # Merge common folders
    merge_common_folders(args.src, args.dst)
    print("Common folders merged successfully.")
