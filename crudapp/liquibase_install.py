import os
import urllib.request
import tarfile

def download_liquibase(url, destination_dir):
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)
    
    # Extract the filename from the URL
    file_name = url.split('/')[-1]
    file_path = os.path.join(destination_dir, file_name)
    
    # Download the file
    with urllib.request.urlopen(url) as response:
        with open(file_path, 'wb') as out_file:
            out_file.write(response.read())
    
    # Extract the tar.gz file
    with tarfile.open(file_path, 'r:gz') as tar:
        tar.extractall(destination_dir)
    
    print(f"Liquibase downloaded and extracted to {destination_dir}")

# Example usage:
liquibase_url = "https://github.com/liquibase/liquibase/releases/download/v4.28.0/liquibase-4.28.0.tar.gz"
destination_directory = "/application/liquibase"
download_liquibase(liquibase_url, destination_directory)
