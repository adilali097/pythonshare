import shutil
import os

def auto_data_sharing(source_folder, destination_folder):
    try:
        # Ensure the source folder exists
        if not os.path.exists(source_folder):
            print(f"Source folder '{source_folder}' does not exist.")
            return

        # Ensure the destination folder exists, create if not
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Created destination folder '{destination_folder}'.")

        # Copy all files from source to destination
        for file_name in os.listdir(source_folder):
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)
            shutil.copy2(source_path, destination_path)
            print(f"Copied: {file_name}")

        print("Data sharing completed successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
source_folder = "C:\Users\khama\Favorites"
destination_folder = "E:\"

auto_data_sharing(source_folder, destination_folder)
