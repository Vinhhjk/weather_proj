import os
import glob

# ... (keep the existing imports)

def delete_json_files():
    files = glob.glob('weather_*.json')
    for file in files:
        os.remove(file)
    print(f"Deleted {len(files)} JSON files.")

# Add this at the beginning of your script to delete existing files before creating new ones
delete_json_files()
