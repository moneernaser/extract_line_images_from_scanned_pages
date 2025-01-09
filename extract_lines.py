import cv2
import numpy as np
import os

# Load image dir from command line
import sys
# if not provided, print usage and exit. User should provide image directory or a single image
if not len(sys.argv) > 1:
    print("Usage: provide an image directory or a single image path.")
    print("Example: python extract_lines.py path/to/image_dir")
    print("Example: python extract_lines.py path/to/image.png")
    sys.exit(1)

output_folder = "extracted_lines"
os.makedirs(output_folder, exist_ok=True)


def extract_lines(image_dir_or_path):
    if os.path.isdir(image_dir_or_path):
        extract_lines_from_dir(image_dir_or_path)
    else:
        extract_lines_from_image(image_dir_or_path)


def extract_lines_from_dir(image_dir):
    for image_path in os.listdir(image_dir):
        if image_path.endswith('.png') or image_path.endswith('.jpg'):
            print(f"Extracting lines from {image_path}")
            extract_lines_from_image(image_path)
            
def extract_lines_from_image(image_path):
    image = cv2.imread(
            image_path, cv2.IMREAD_GRAYSCALE)


    # Threshold the image
    _, binary_image = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find horizontal projection
    horizontal_projection = np.sum(binary_image, axis=1)

    # Identify line boundaries
    line_indices = []
    in_line = False
    for i, value in enumerate(horizontal_projection):
        if value > 0 and not in_line:  # Start of a line
            start = i
            in_line = True
        elif value == 0 and in_line:  # End of a line
            end = i
            in_line = False
            line_indices.append((start, end))

    # Extract lines
    line_images = []
    for start, end in line_indices:
        line_image = binary_image[start:end, :]
        line_images.append(line_image)
        # Save individual line images
        image_name = image_path.split('/')[-1]
        # write to output folder in this directory
        cv2.imwrite(f"{output_folder}/{image_name}_{start}_{end}.png", line_image)
        

    print(f"Extracted {len(line_images)} lines.")


extract_lines(sys.argv[1])