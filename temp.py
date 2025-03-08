import os

dataset_path = "C:/Users/ianmk/CODING/val_vision/killfeed/dataset"

for root, dirs, files in os.walk(dataset_path):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            with open(file_path, "r") as f:
                pass  # Try opening the file
        except PermissionError:
            print(f"Permission Denied: {file_path}")
