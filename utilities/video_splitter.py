import os
import cv2
import math
import tkinter as tk
from tkinter import filedialog

def get_file_size(file_path):
    """Get the file size in bytes."""
    return os.path.getsize(file_path)

def split_video(input_path, output_dir, max_size=25 * 1024 * 1024):
    """Split the video into segments each no larger than max_size bytes."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    video_size = get_file_size(input_path)  # in bytes
    target_duration = max_size / video_size * duration
    num_parts = math.ceil(duration / target_duration)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    codec = cv2.VideoWriter_fourcc(*'mp4v')

    for part_number in range(num_parts):
        start_time = part_number * target_duration
        end_time = min((part_number + 1) * target_duration, duration)
        new_filename = os.path.join(output_dir, f'part_{part_number + 1}.mp4')

        out = cv2.VideoWriter(new_filename, codec, fps, (width, height))
        cap.set(cv2.CAP_PROP_POS_MSEC, start_time * 1000)

        while cap.get(cv2.CAP_PROP_POS_MSEC) < end_time * 1000:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)

        out.release()

    cap.release()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    input_path = filedialog.askopenfilename(title="Select the video file", filetypes=[("Video files", "*.mp4 *.mov")])
    output_dir = filedialog.askdirectory(title="Select the output directory")

    if input_path and output_dir:
        split_video(input_path, output_dir)
        print("Video has been split successfully.")
    else:
        print("Operation cancelled.")
