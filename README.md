# Download Organizer Project

A Python script to automatically sort files in your Downloads folder into subfolders based on file type.

## How It Works
- Scans the Downloads folder.
- Moves files into folders like `Images`, `Documents`, `Videos`, or `Misc` based on extensions.

## Supported File Types
- **Images:** .jpg, .png, .jpeg
- **Documents:** .pdf, .txt, .docx, .docs
- **Videos:** .mp4, .mov
- **Music:** .mp3, .wav, .aiff
- **Misc:** Anything else

## How to Use
1. Clone the repo: `git clone https://github.com/rmnsmbln/Download_Organizer_Project.git`
2. Run: `python organizer.py`

## Scheduling on macOS
To run every 5 minutes:
1. Open Terminal and run: `crontab -e`
2. Add this line: `*/5 * * * * /usr/bin/python3 /Users/ramsimbulan/Desktop/Download_Organizer_Project/organizer.py`
3. Save and exit (in vi: Esc, :wq, Enter).