# Extract Line Images

This script extracts lines from images and saves them as individual image files. It can process a single image or all images in a directory.

Example `scanned_image.png` in included.

## Usage

To run the script, use the following command:
```sh
python extract_lines.py <path_to_image_or_directory>
```

Replace `<path_to_image_or_directory>` with the path to your image file or directory containing images.

## Example

To process a single image:
```sh
python extract_lines.py path/to/image.png
```

To process all images in a directory:
```sh
python extract_lines.py path/to/image_dir
```