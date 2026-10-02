import os
from PIL import Image

def convert_webp_to_jpg(webp_file, output_folder):
    try:
        # Open WEBP image
        image = Image.open(webp_file).convert('RGB')  # Ensure it's in RGB mode

        # Construct the output file path with .jpg extension
        jpg_file = os.path.join(
            output_folder,
            os.path.basename(webp_file).replace('.webp', '.jpg').replace('.WEBP', '.jpg')
        )

        # Save as JPG
        image.save(jpg_file, "JPEG")
        print(f"Converted: {webp_file} to {jpg_file}")
    except Exception as e:
        print(f"Failed to convert {webp_file}: {e}")

def main():
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(current_directory, 'Converted')

    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert all WEBP files in the current directory
    webp_files_found = False
    for file in os.listdir(current_directory):
        if file.lower().endswith('.webp'):
            webp_file_path = os.path.join(current_directory, file)
            convert_webp_to_jpg(webp_file_path, output_folder)
            webp_files_found = True

    if not webp_files_found:
        print("No WEBP files found in the current directory.")

if __name__ == "__main__":
    main()
