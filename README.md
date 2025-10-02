📌 Image Resizer Tool

This project is a simple batch image resizer built with Python and the Pillow library. It automatically resizes all images inside a given folder while maintaining the aspect ratio.

🎯 Objective

- Resize multiple images in bulk.
- Maintain aspect ratio while resizing.
- Skip images that are already smaller than the target width.

🛠️ Tools & Technologies

- Python (3.x)
- Pillow (PIL fork)
- Install Pillow:
     pip install pillow

🚀 How to Run
- Clone or download this project.
- Place the images you want to resize inside the input_images folder.
- Run the script:
    python resize_images.py
- Resized images will be saved inside the output_images folder with names like:
  resized_sample.jpg
  resized_logo.png

⚙️ Configuration

- You can edit these variables at the top of resize_images.py:

INPUT_FOLDER = 'input_images'      # Folder where original images are stored
OUTPUT_FOLDER = 'output_images'    # Folder to save resized images
NEW_WIDTH = 400                    # Target width (px) for resized images

- The script automatically calculates the height to preserve aspect ratio.
- Images smaller than NEW_WIDTH are skipped.

📊 Features

✔️ Batch resize multiple images
✔️ Preserves aspect ratio
✔️ Supports common formats: .png, .jpg, .jpeg, .gif, .bmp
✔️ Error handling for missing/invalid files
✔️ Skips non-image files automatically

🎯 Outcome

This tool automates repetitive image resizing tasks, making it useful for:

- Preparing images for websites
- Optimizing photos for reports/presentations
- Reducing file size before uploads
