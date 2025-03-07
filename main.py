import os
import shutil

print("Welcome to Downloads Organizer")

# Define directory path
downloads_path = os.path.expanduser("~/Downloads")
print(f"Scanning: {downloads_path}")

# Define file types and their respected fodlers
file_types = {
  "Images": [".jpg", ".png", ".jpeg"],
  "Documents": [".pdf", ".txt", ".doc", ".docx"],
  "Music": [".mp3", ".wav", ".aiff"],
  "Videos": [".mp4", ".mov"],
  "Misc": []
}

# Organize the files
for file in os.listdir(downloads_path):
  file_path = os.path.join(downloads_path, filename)
  if os.path.isfile(file_path):
    # Split file name and extension
    _, ext = os.path.splitext(file)
    ext = ext.lower()

    # Find the right folder
    target_folder = "Misc"
    for folder, extentions in file_types.items():
      if ext in extentions:
        target_folder = folder
        break
    
    