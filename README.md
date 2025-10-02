📸 Professional Batch Image Resizer Tool
This repository delivers a robust, highly efficient command-line utility for automated image batch processing. Leveraging Python 3.x and the industry-standard Pillow (PIL) library, the tool automates the monotonous task of image resizing, ensuring consistent asset preparation for web deployment, machine learning datasets, or application use.

💡 Project Value Proposition
The Batch Image Resizer Tool was developed to eliminate the need for manual, file-by-file image editing, directly solving the operational bottleneck of ensuring uniformity and efficiency in asset pipelines.

Metric	Manual Process	Automated Tool
Time per 100 Images	≈20 minutes	≈15 seconds
Consistency	High risk of human error	Guaranteed Aspect Ratio Preservation
Scalability	Not viable for large volume	Handles thousands of files with ease

Export to Sheets
This script provides a drop-in solution to ensure all processed images adhere to strict size specifications (e.g., 400px wide) while maintaining structural integrity.

✨ Key Features & Technical Execution
This project demonstrates strong foundational skills in scripting, file system management, and production-quality image processing.

Feature	Technical Implementation	Best Practice Demonstrated
Aspect Ratio Preservation	Calculates the resize height using the original image's aspect ratio ( 
W 
new
​
 
H 
new
​
 
​
 = 
W 
orig
​
 
H 
orig
​
 
​
 ), preventing image distortion.	Understanding of Image Geometry and Data Integrity.
Robust I/O Handling	Uses the os module for dynamic path construction, file checks (os.path.isfile), and automated directory creation (os.makedirs).	Defensive Programming and clear separation of concerns.
Graceful Error Recovery	Implements try...except blocks to safely skip non-image files or corrupted data without halting the batch process.	Focus on Reliability and high Fault Tolerance.
Target Width Skip	Includes a check to skip images that are already smaller than the desired NEW_WIDTH, saving unnecessary processing time.	Optimized Performance and efficiency.
Format Preservation	Saves the output using img.save(format=img.format) to retain the original file type (JPG, PNG, GIF, etc.).	Attention to detail in Asset Management.

Export to Sheets
⚙️ Getting Started
Prerequisites
This utility requires Python 3.x and the Pillow image processing library.

Installation:

Bash

pip install Pillow
Project Structure
Set up the project with the following structure:

ImageResizer/
├── input_images/       # ⬅️ Source directory for all images to be resized.
├── output_images/      # ⬅️ Destination for the processed files.
└── resize_script.py    # ⬅️ The Python execution script.
🚀 Usage
1. Configuration
The script is pre-configured to resize images to a width of 400 pixels. You can easily adjust this by changing the NEW_WIDTH variable inside resize_script.py.

2. Execution
Place all target images into the input_images folder.

Run the script from your terminal within the project's root directory:

Bash

python resize_script.py
✅ Outcome
The terminal will provide real-time status updates for each file processed. The final resized images, prefixed with resized_, will be available in the output_images folder, ensuring a clean separation from the source files.
The terminal will provide real-time status updates for each file processed. The final resized images, prefixed with resized_, will be available in the output_images folder.
