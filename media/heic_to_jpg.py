import os
import sys
from PIL import Image
import pyheif

def convert_heic_to_jpg(heic_file, output_folder):
    try:
        # Load HEIC file
        heif_file = pyheif.read(heic_file)

        # Convert to RGB
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )

        # Construct the output file path with .jpg extension
        jpg_file = os.path.join(output_folder, os.path.basename(heic_file).replace('.heic', '.jpg').replace('.HEIC', '.jpg'))

        # Save as JPG
        image.save(jpg_file, "JPEG")
        print(f"Converted: {heic_file} to {jpg_file}")
    except Exception as e:
        print(f"Failed to convert {heic_file}: {e}")

def main():
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(current_directory, 'Converted')

    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert all HEIC files in the current directory
    heic_files_found = False
    for file in os.listdir(current_directory):
        if file.lower().endswith('.heic'):
            heic_file_path = os.path.join(current_directory, file)
            convert_heic_to_jpg(heic_file_path, output_folder)
            heic_files_found = True

    if not heic_files_found:
        print("No HEIC files found in the current directory.")

if __name__ == "__main__":
    main()
