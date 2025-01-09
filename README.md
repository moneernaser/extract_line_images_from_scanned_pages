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

## Setup

Before running the script, ensure you have the required dependencies installed. You can set up a virtual environment and install the dependencies using the following steps.

### Windows

1. Open Command Prompt.
2. Navigate to the project directory:
    ```sh
    cd /path/to/extract_line_images
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    ```sh
    venv\Scripts\activate
    ```
5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Mac

1. Open Terminal.
2. Navigate to the project directory:
    ```sh
    cd /path/to/extract_line_images
    ```
3. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    ```sh
    source venv/bin/activate
    ```
5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
