import glob
import shutil
import os

# Checking the given directory for .zip files
for file in glob.glob('~/Downloads/*.zip'):
    
    # Extracting the name of the .zip file without the extension
    zip_name = os.path.splitext(os.path.basename(file))[0]
    
    destination_path = os.path.join('/home/martin/Downloads/unzipped/', zip_name)
    
    # Unzipping the folder
    shutil.unpack_archive(file, destination_path)
    
    # Deleting the original .zip file
    os.remove(file)