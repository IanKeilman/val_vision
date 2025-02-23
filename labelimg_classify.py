import os
import shutil
import subprocess
import re

# Path to Frames directory
frames_dir = "Frames"

# Path to the temporary directory for filtered and renamed images
filtered_dir = "FilteredFrames"

# Clear and recreate the filtered folder
if os.path.exists(filtered_dir):
    shutil.rmtree(filtered_dir)  # Remove old files
os.makedirs(filtered_dir)

# Function to extract required name format from folder name
def format_folder_name(folder_name):
    # Split folder name by spaces and dashes
    parts = re.split(r" - | ", folder_name)
    
    if len(parts) < 4:  # Ensure we have enough words
        return None
    
    first_word = parts[0]   # First word (e.g., VIT)
    second_word = parts[1]  # Second word (e.g., DRX)
    last_two_words = "_".join(parts[-2:]).lower()  # Last two words (e.g., "map_01")

    return f"{first_word}_{second_word}_{last_two_words}"

# Iterate through each subfolder in Frames
for subfolder in os.listdir(frames_dir):
    subfolder_path = os.path.join(frames_dir, subfolder)
    
    if os.path.isdir(subfolder_path):
        formatted_name = format_folder_name(subfolder)
        if not formatted_name:
            continue  # Skip folders that don't fit the pattern

        for filename in os.listdir(subfolder_path):
            # Only include "frame_XXX" (without extra suffixes like _minimap, _killfeed, _score)
            if filename.startswith("frame_") and "_" not in filename[6:]:  
                src_path = os.path.join(subfolder_path, filename)

                frame_number = filename.split("_")[1].split(".")[0]  # Remove extension
                frame_number = int(frame_number)  # Convert to integer
                new_filename = f"{formatted_name}_frame_{frame_number:03d}.png"

                dest_path = os.path.join(filtered_dir, new_filename)

                # Copy the file with the new name
                shutil.copy2(src_path, dest_path)  

# Launch LabelImg in the filtered directory
subprocess.run(["labelImg", filtered_dir])

