📸 Batch Image Resizer Tool
This repository contains a simple, yet powerful command-line script for batch processing images. Built with Python and the Pillow (PIL) library, the tool automatically reads all images from a specified input folder, resizes them to a target width while maintaining their aspect ratio, and saves the new files to an output folder.

📌 Project Summary
The Batch Image Resizer Tool is designed to automate the repetitive task of resizing large collections of images. It is ideal for quickly preparing image assets for web deployment, machine learning datasets, or any application requiring uniform image dimensions.

The script demonstrates proficiency in:

File System Automation: Using the os module to navigate directories and handle files.

Image Processing: Utilizing the Pillow library for core image manipulation.

Error Handling: Ensuring the script can handle non-image files or corrupted images gracefully.

✨ Key Features
Feature	Description	Technology Demonstrated
Batch Processing	Automatically iterates through every file in the input directory.	os.listdir(), os.path
Aspect Ratio Preservation	Calculates the new height dynamically to prevent image stretching/distortion.	Pillow (Image.open(), img.size)
Input/Output Management	Separate folders for source images and processed images, keeping the project organized.	os.makedirs(), os.path.join()
File Type Support	Supports common image formats including JPG, PNG, GIF, and BMP.	Pillow (img.save(format=...))

Export to Sheets
⚙️ Getting Started
Follow these steps to set up and run the script on your local machine.

Prerequisites
You must have Python 3.x installed. The project relies on the Pillow library.

Install Pillow:

Bash

pip install Pillow
# or
pip3 install Pillow
Project Structure
Set up the following directory structure:

ImageResizer/
├── input_images/       <-- PLACE YOUR ORIGINAL IMAGES HERE
├── output_images/      <-- RESIZED IMAGES WILL BE SAVED HERE
└── resize_script.py    <-- THE PYTHON SCRIPT
🚀 How to Run the Tool
1. Place Images
Put all the images you want to resize inside the input_images folder.

2. Configure the Script (Optional)
Open resize_script.py and modify the NEW_WIDTH variable to your desired target width (default is 400 pixels):

Python

# --- Configuration ---
INPUT_FOLDER = 'input_images'
OUTPUT_FOLDER = 'output_images'
NEW_WIDTH = 400 # <--- CHANGE THIS VALUE
# ---------------------
3. Execute the Script
Run the Python script from your terminal:

Bash

python resize_script.py
# or
python3 resize_script.py
🎯 Outcome
Upon successful execution, the terminal will display a summary of processed files, and the output_images folder will be automatically populated with the resized versions of your input images, prefixed with resized_.

🛠 Technology Stack
Language: Python 3.x

Core Library: Pillow (PIL)

Modules: os (for file system interaction)
