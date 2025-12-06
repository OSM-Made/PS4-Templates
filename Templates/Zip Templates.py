import os
import zipfile

def zip_directory_contents():
    """
    Looks at all directories adjacent to this script, zips their contents
    (including subfolders), and names the zip file after the directory.

    Contents are placed at the root of the zip (no top-level folder inside).
    """
    
    # 1. Get the current working directory where the script is located
    current_dir = os.getcwd()
    print(f"Starting archival process in: {current_dir}")
    print("-" * 30)

    # 2. Iterate through all items in the current directory
    for item_name in os.listdir(current_dir):
        # Construct the full path to the item
        item_path = os.path.join(current_dir, item_name)

        # 3. Check if the item is a directory (folder) and NOT the script's own file
        if os.path.isdir(item_path) and item_name != os.path.basename(__file__):
            
            # This is the directory we want to archive
            source_dir = item_path
            
            # Define the output zip file name (e.g., 'assets.zip')
            zip_filename = f"{item_name}.zip"
            zip_filepath = os.path.join(current_dir, zip_filename)

            print(f"Archiving folder: **{item_name}** to **{zip_filename}**")

            try:
                # 4. Open the zip file in write mode ('w')
                with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    # os.walk traverses the directory tree
                    for root, dirs, files in os.walk(source_dir):
                        for file in files:
                            # a. Full path to the file on the disk
                            file_path = os.path.join(root, file)
                            
                            # b. The crucial step: calculate the path *inside* the zip file (arcname)
                            # os.path.relpath calculates the path relative to the 'source_dir', 
                            # ensuring the contents start at the zip's root.
                            arc_name = os.path.relpath(file_path, source_dir)
                            
                            # Add the file to the zip with the correct internal path
                            zipf.write(file_path, arc_name)

                print(f"Successfully created: {zip_filename}")
            
            except Exception as e:
                print(f"Failed to archive {item_name}. Error: {e}")

            print("-" * 30)

if __name__ == "__main__":
    zip_directory_contents()