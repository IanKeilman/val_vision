import os

def create_empty_annotations(image_folder, label_folder):
    # Ensure the label folder exists
    os.makedirs(label_folder, exist_ok=True)
    
    # Get a list of image filenames (without extension)
    image_filenames = {os.path.splitext(f)[0] for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))}
    
    # Get a list of annotation filenames (without extension)
    annotation_filenames = {os.path.splitext(f)[0] for f in os.listdir(label_folder) if f.endswith(('.txt', '.xml'))}
    
    # Find images without corresponding annotation files
    missing_annotations = image_filenames - annotation_filenames
    
    for img_name in missing_annotations:
        annotation_path = os.path.join(label_folder, f"{img_name}.txt")
        with open(annotation_path, 'w') as f:
            pass  # Create an empty file
        print(f"Created empty annotation: {annotation_path}")
    
    print("Done. All images now have annotations.")

# Example usage
label_folder = "killfeed/annotations"  # Replace with your images folder path
image_folder = "killfeed/images"  # Replace with your labels folder path
create_empty_annotations(image_folder, label_folder)
