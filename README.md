# python-toolkit

A growing collection of small, single-purpose Python scripts I've written to automate the little tasks that come up in day-to-day IT and desktop work.

> **If I do it twice, I automate it.** Each of these started as something I'd done by hand one too many times.

Nothing here needs a framework or a server. Every script is standalone: drop it where you need it, run it, done. Most prompt for what they need or pick up files from the folder they're run in.

## What's inside

### 📁 `media/` — file conversion
| Script | Does |
|---|---|
| `heic_to_jpg.py` | Convert iPhone HEIC photos to JPG |
| `webp_to_jpg.py` | Convert WEBP images to JPG |
| `mp4_to_mov.py` | Convert MP4 videos to MOV |
| `video_to_mp3.py` | Pull the audio out of video files as MP3 |
| `video_to_gif.py` | Turn a video clip into a GIF, with size presets |
| `combine_audio_and_video.py` | Mux a separate audio and video track into one file |

### 📁 `office/` — documents
| Script | Does |
|---|---|
| `pdf_to_docx.py` | Extract text from PDFs into editable Word documents |
| `word_to_pdf.py` | Convert a `.docx` to PDF |
| `clipboard_to_docx.py` | Save whatever's on your clipboard straight to a Word doc |
| `clipboard_to_txt.py` | Save the clipboard to a text file |
| `outlook_email_to_docx.py` | Grab the latest Outlook email (macOS) and save it as a Word doc |

### 📁 `utilities/` — everyday helpers
| Script | Does |
|---|---|
| `location_lookup.py` | Latitude/longitude for a place name |
| `location_by_ip.py` | Approximate location of the current machine by IP |
| `date_lapse_calculator.py` | How long since a timestamp — handy for "last seen online" lines in remote-support logs |
| `video_splitter.py` | Split a video into chunks under a size limit (e.g. for upload caps) |

### 📁 `security/` — passwords
| Script | Does |
|---|---|
| `password_generator.py` | Generate strong passwords (uses `SystemRandom`), with optional custom words |
| `password_generator_exclude_chars.py` | Same idea, but exclude characters that cause trouble in certain fields |

## Running them

Each script is independent. Install only what the script you want uses:

```bash
pip install -r requirements.txt   # everything, or
pip install pillow pyheif          # just what a given script needs
```

The media scripts call **ffmpeg**, which is a system tool, not a pip package:

```bash
brew install ffmpeg
```

The scripts look for `ffmpeg` on your `PATH` automatically and fall back to a common Homebrew location.

Then run whatever you need:

```bash
python media/heic_to_jpg.py
python utilities/location_lookup.py
```

## Notes

- These are practical tools, not a polished library — they favour "works and saves me time" over abstraction.
- Scripts that save output default to your Desktop or the folder they're run in.
- This repo grows as I run into new annoyances worth automating.

## License

[MIT](LICENSE).
