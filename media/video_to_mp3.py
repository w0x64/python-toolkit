import os
import shutil
import subprocess

FFMPEG_PATH = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"  # falls back to a common Homebrew path
AUDIO_BITRATE = "192k"

def convert_to_mp3(input_folder):
    supported_extensions = (".mov", ".mp4", ".m4a")

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(supported_extensions):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(
                input_folder, os.path.splitext(file_name)[0] + ".mp3"
            )

            # Skip if MP3 already exists
            if os.path.exists(output_file_path):
                print(f"Skipping (already exists): {output_file_path}")
                continue

            command = [
                FFMPEG_PATH,
                "-y",                 # overwrite without asking
                "-i", input_file_path,
                "-vn",                # no video
                "-ar", "44100",
                "-ac", "2",
                "-ab", AUDIO_BITRATE,
                output_file_path
            ]

            print(f"Converting: {file_name}")
            subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    convert_to_mp3(script_directory)
    print("✅ Conversion completed.")

if __name__ == "__main__":
    main()
