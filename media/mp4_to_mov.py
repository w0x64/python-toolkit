import os
import subprocess
import shutil
FFMPEG = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"  # falls back to a common Homebrew path

def convert_mp4_to_mov(input_folder):
    # Iterate over all files in the input folder
    for file_name in os.listdir(input_folder):
        # Check if the file is an MP4 file
        if file_name.endswith(".mp4"):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(input_folder, file_name[:-4] + ".mov")

            # Define the ffmpeg command
            command = [FFMPEG, "-i", input_file_path, output_file_path]

            # Convert MP4 to MOV
            subprocess.run(command)

def main():
    # Get the current directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))

    convert_mp4_to_mov(script_directory)
    
    print("Conversion completed.")

if __name__ == "__main__":
    main()
