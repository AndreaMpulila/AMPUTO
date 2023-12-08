from PIL import Image
import os

def convertToWebp(input_path, output_path, quality=80):
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Save the image in WebP format
            img.save(output_path, "WEBP", quality=quality)
            print(f"Conversion successful: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error converting {input_path} to WebP: {e}")

def batchConvertToWebp(input_folder, output_folder, quality=80):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpeg", ".jpg")):
            input_path = os.path.join(input_folder, filename)
            # Change the file extension to webp
            output_filename = os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(output_folder, output_filename)
            # Convert the image to WebP
            convertToWebp(input_path, output_path, quality)

# Example usage
input_folder = input("Input Image Containing Folder Path : ")
output_folder = input("Input Folder to Store Image Result: ")
batchConvertToWebp(input_folder, output_folder)
