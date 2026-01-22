"""
This is a simple file organizer script in Python that organizes files in my downloads folder into subfolders based on their file types.
It categorizes files into folders such as Images, Documents, Videos, Music, and Others.

Author: Zane Francis
"""
import os
import shutil

# Resolve the Downloads folder, preferring an existing path (OneDrive vs local).
candidate_sources = [
    os.path.join(os.path.expanduser('~'), 'Downloads'),
    os.path.join(os.path.expanduser('~'), 'OneDrive', 'Downloads'),
]
source_dir = next((p for p in candidate_sources if os.path.isdir(p)), candidate_sources[0])

# Define the target directories for different file types
target_dirs = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Others': []
}

# Skip active/incomplete downloads and temporary files.
ignored_extensions = {'.crdownload', '.part', '.tmp', '.download'}

def move_file_safe(src_path: str, dest_dir: str, filename: str) -> None:
    """Move file to dest_dir, auto-renaming to avoid collisions."""
    base, ext = os.path.splitext(filename)
    candidate = filename
    counter = 1

    while os.path.exists(os.path.join(dest_dir, candidate)):
        candidate = f"{base} ({counter}){ext}"
        counter += 1

    shutil.move(src_path, os.path.join(dest_dir, candidate))

def organize_files():
    # Create target directories if they don't exist
    for folder in target_dirs.keys():
        folder_path = os.path.join(source_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Iterate through files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        try:
            # Get the file extension
            file_ext = os.path.splitext(filename)[1].lower()

            if file_ext in ignored_extensions:
                continue
            moved = False

            # Check which category the file belongs to and move it
            for folder, extensions in target_dirs.items():
                if file_ext in extensions:
                    move_file_safe(file_path, os.path.join(source_dir, folder), filename)
                    moved = True
                    break
            
            # If the file doesn't match any category, move it to 'Others'
            if not moved:
                move_file_safe(file_path, os.path.join(source_dir, 'Others'), filename)
        except Exception as exc:  # Keep processing on individual file failures
            print(f"Skipped {filename}: {exc}")
        
if __name__ == "__main__":
    organize_files()
    print("Files have been organized successfully.")