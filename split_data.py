import os
from tqdm import tqdm
import random
import shutil

def split_data(source_folder, dest_train_folder, dest_valid_folder, split_ratio=0.8):
    # Check if the source folder path is valid
    if not os.path.exists(source_folder):
        print("Source folder does not exist. Please provide a valid path.")
        return

    # Create destination folders if they don't exist
    os.makedirs(dest_train_folder, exist_ok=True)
    os.makedirs(dest_valid_folder, exist_ok=True)

    os.makedirs(os.path.join(dest_train_folder, "images"), exist_ok=True)
    os.makedirs(os.path.join(dest_train_folder, "labels"), exist_ok=True)
    os.makedirs(os.path.join(dest_valid_folder, "images"), exist_ok=True)
    os.makedirs(os.path.join(dest_valid_folder, "labels"), exist_ok=True)

    # Get a list of all image files in the source folder
    image_files = [file for file in os.listdir(os.path.join(source_folder, "images")) if file.endswith((".jpg", ".jpeg", ".png"))]

    # Display the total number of images
    total_images = len(image_files)
    print(f"Total Number of Images: {total_images}")

    # Calculate the number of images for training and testing
    num_train = int(total_images * split_ratio)
    num_test = total_images - num_train

    # Randomly shuffle the list of image files
    random.shuffle(image_files)

    # Copy the first 'num_train' images to the training folder
    for file in tqdm(image_files[:num_train]):
        shutil.copy(os.path.join(source_folder, "images", file), os.path.join(dest_train_folder, "images"))
        shutil.copy(os.path.join(source_folder, "labels", file.replace(".jpg", ".txt").replace(".jpeg", ".txt").replace(".png", ".txt")), os.path.join(dest_train_folder, "labels"))

    # Copy the remaining images to the testing folder
    for file in tqdm(image_files[num_train:]):
        shutil.copy(os.path.join(source_folder, "images", file), os.path.join(dest_valid_folder, "images"))
        shutil.copy(os.path.join(source_folder, "labels", file.replace(".jpg", ".txt").replace(".jpeg", ".txt").replace(".png", ".txt")), os.path.join(dest_valid_folder, "labels"))

    # Display the total counts after splitting
    print(f"Total Images in Training Set: {num_train} copied into train folder")
    print(f"Total Images in Testing Set: {num_test} copied into the valid folder")

if __name__ == "__main__":
    source_folder = "activity_train_data_v10.1"
    dest_train_folder = "train"
    dest_valid_folder = "valid"

    # Check if the source folder path is valid
    if not os.path.exists(source_folder):
        print("Source folder does not exist. Please provide a valid path.")
    else:
        split_data(source_folder, dest_train_folder, dest_valid_folder)
