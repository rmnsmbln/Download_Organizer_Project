import os
import shutil

print("Welcome to Downloads Organizer!")
print("-------------------------------")

# Define directory path
downloads_path = os.path.expanduser("~/Downloads")
print(f"Looking at: {downloads_path}")

# Define file types and their respected folders
file_types = {
  "Images": [".jpg", ".png", ".jpeg"],
  "Documents": [".pdf", ".txt", ".doc", ".docx"],
  "Music": [".mp3", ".wav", ".aiff"],
  "Videos": [".mp4", ".mov"],
  "Misc": []
}

# Organize the files
for file in os.listdir(downloads_path):
  file_path = os.path.join(downloads_path, file)
  if os.path.isfile(file_path):
    print(f"Found: {file}")
    # Split file name and extension
    _, ext = os.path.splitext(file)
    ext = ext.lower()

    # Find the right folder
    target_folder = "Misc"
    for folder, extentions in file_types.items():
      if ext in extentions:
        target_folder = folder
        break
    
    # Create the folder if it doesn't exist yet
    target_path = os.path.join(downloads_path, target_folder)
    if not os.path.exists(target_path):
      os.makedirs(target_path)

    # Then move the files to the correct folders
    new_file_path = os.path.join(target_path, file)
    print(f"Moving {file} to {target_folder}")
    shutil.move(file_path, new_file_path)