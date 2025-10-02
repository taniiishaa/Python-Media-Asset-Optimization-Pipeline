import os
from PIL import Image

# --- Configuration ---
INPUT_FOLDER = 'input_images'
OUTPUT_FOLDER = 'output_images'
NEW_WIDTH = 400 # The desired width in pixels for all output images
# ---------------------

def resize_image(image_path, output_path, new_width):
    """Opens, resizes, and saves a single image while preserving aspect ratio."""
    try:
        # 1. Open the image
        img = Image.open(image_path)
        
        # 2. Calculate the new height to maintain aspect ratio
        original_width, original_height = img.size
        
        # Check if the image is already smaller than the target width
        if original_width <= new_width:
            print(f"Skipping {os.path.basename(image_path)}: Already smaller than {new_width}px wide.")
            return

        ratio = original_height / original_width
        new_height = int(new_width * ratio)
        
        # 3. Resize the image using the calculated dimensions
        resized_img = img.resize((new_width, new_height))
        
        # 4. Save the resized image
        # We save it using the original file's format (e.g., .jpg, .png)
        resized_img.save(output_path, img.format)
        
        print(f"SUCCESS: Resized {os.path.basename(image_path)} to {new_width}x{new_height}")
        
    except FileNotFoundError:
        print(f"ERROR: Image file not found at {image_path}")
    except Exception as e:
        print(f"ERROR: Could not process {os.path.basename(image_path)}. Reason: {e}")


def batch_resize(input_dir, output_dir, new_width):
    """Loops through a directory and calls resize_image for all image files."""
    
    # 1. Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"INFO: Created output directory: {output_dir}")

    print(f"\nProcessing images in {input_dir}...")
    
    # 2. Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        # Construct the full file paths
        input_filepath = os.path.join(input_dir, filename)
        
        # 3. Only process actual files
        if os.path.isfile(input_filepath):
            # Check for common image file extensions
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                
                # Define the output filename: e.g., 'resized_image1.jpg'
                output_filepath = os.path.join(output_dir, f"resized_{filename}")
                
                resize_image(input_filepath, output_filepath, new_width)
            else:
                print(f"SKIPPED: Non-image file or unknown type: {filename}")


# --- Script Execution ---
if __name__ == "__main__":
    batch_resize(INPUT_FOLDER, OUTPUT_FOLDER, NEW_WIDTH)
    print("\n--- Batch resize process complete! ---")