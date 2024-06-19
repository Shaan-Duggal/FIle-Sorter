import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Downloads")

extensions = {
    ".jpg": "Images",
    ".svg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".heic": "Images",
    ".webp": "Images",
    ".tiff": "Images",
    ".avif": "Images",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".mkf": "Videos",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".pages": "Documents",
    ".rtf": "Documents",
    ".epub": "Documents",
    ".mp3": "Music",
    ".wav": "Music",
    ".m4a": "Music",
    ".aiff": "Music",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".key": "Presentations",
    ".zip": "Compressed files",
    ".rar": "Compressed files",
    ".7z": "Compressed files",
    ".dmg": "Compressed files"
}

# List all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
        
    # Check if it's a file and not a directory
    if os.path.isfile(file_path):
        # Extract the file extension
        extension = os.path.splitext(filename)[1].lower()  # Skip the dot and convert to lower case
            
        # Check if the extension is in our dictionary
        if extension in extensions:
            folder_name = extensions[extension]
            folder_path = os.path.join(directory, folder_name)
                
            # Create the folder if it does not exist
            os.makedirs(folder_path, exist_ok=True)
                
            # Build the destination path
            destination_path = os.path.join(folder_path, filename)
                
            # Move the file
            shutil.move(file_path, destination_path)
            print(f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"Skipped {filename}. Unknown file extension.")
    else:
        print(f"Skipped {filename}. It is a directory.")

print("File organization completed.")
