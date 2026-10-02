import os
import shutil
import subprocess
import tkinter as tk
from tkinter import simpledialog, filedialog

def convert_video_to_gif(input_path, output_path, width, height):
    """Convert a video file to GIF using ffmpeg."""
    ffmpeg_path = shutil.which("ffmpeg") or "/usr/local/bin/ffmpeg"  # falls back to a common path
    scale_str = f"scale={width}:{height}:flags=lanczos"
    cmd = [
        ffmpeg_path,
        '-i', input_path,
        '-vf', f"fps=10,{scale_str}",
        '-c:v', 'gif',
        output_path
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    input_path = filedialog.askopenfilename(title="Select the video file", filetypes=[("Video files", "*.mp4 *.mov")])
    output_dir = filedialog.askdirectory(title="Select the output directory")

    if input_path and output_dir:
        size_choices = {
            "1": (320, 240),   # Small
            "2": (640, 480),   # Medium
            "3": (1280, 720),  # Large
            "4": "Custom"      # Custom size
        }

        size_prompt = (
            "Choose the size for the GIF:\n"
            "1. Small (320x240)\n"
            "2. Medium (640x480)\n"
            "3. Large (1280x720)\n"
            "4. Custom\n"
            "Enter the number corresponding to your choice: "
        )

        size_choice = simpledialog.askstring("Size Selection", size_prompt)

        if size_choice in size_choices:
            if size_choice == "4":
                width = simpledialog.askinteger("Custom Width", "Enter the width:")
                height = simpledialog.askinteger("Custom Height", "Enter the height:")
            else:
                width, height = size_choices[size_choice]

            video_name = os.path.splitext(os.path.basename(input_path))[0]
            output_path = os.path.join(output_dir, f"{video_name}.gif")
            convert_video_to_gif(input_path, output_path, width, height)
            print(f"GIF has been created successfully: {output_path}")
        else:
            print("Invalid choice. Operation cancelled.")
    else:
        print("Operation cancelled.")
