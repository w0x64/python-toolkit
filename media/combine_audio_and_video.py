import os
import shutil
import subprocess
import string

# Dynamically find the ffmpeg executable path
def get_ffmpeg_path():
    ffmpeg_path = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"  # falls back to a common Homebrew path
    if not ffmpeg_path:
        raise FileNotFoundError("ffmpeg not found in your PATH. Please install ffmpeg.")
    return ffmpeg_path

DEFAULT_SAVE_PATH = os.path.dirname(os.path.abspath(__file__))

def combine_video_audio(folder_path):
    """Combine video and audio files into a single file using ffmpeg."""
    video_file = None
    audio_file = None
    
    # Iterate through files in the folder to find suitable video and audio
    for file in os.listdir(folder_path):
        if (file.endswith('.mp4') or file.endswith('.webm')) and 'combined' not in file:
            video_file = os.path.join(folder_path, file)
        elif file.endswith('.mp3'):
            audio_file = os.path.join(folder_path, file)
    
    # If both video and audio files are found
    if video_file and audio_file:
        title = ''.join(c for c in os.path.basename(video_file)[:-4] if c in string.ascii_letters + string.digits + "-_.() ")
        combined_video_path = os.path.join(folder_path, f"{title}_combined.mp4")
        
        try:
            # Get the path to ffmpeg
            ffmpeg_path = get_ffmpeg_path()
            print(f"Using ffmpeg at: {ffmpeg_path}")

            # Run the ffmpeg command to combine the video and audio
            command = [
                ffmpeg_path, '-i', video_file, '-i', audio_file,
                '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', combined_video_path
            ]
            subprocess.run(command, check=True)

            # Clean up individual files
            os.remove(video_file)
            os.remove(audio_file)

            print(f"Combination and conversion completed for {title}!")
        except FileNotFoundError as e:
            print(e)
        except subprocess.CalledProcessError as e:
            print(f"Error during ffmpeg processing: {e}")
    else:
        print("No suitable video or audio files found.")

if __name__ == "__main__":
    combine_video_audio(DEFAULT_SAVE_PATH)
