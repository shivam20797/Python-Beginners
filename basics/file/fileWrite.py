# file open in write mode

import os
from pathlib import Path

base_dir = Path.cwd()   # current working directory
file_path = base_dir / "basics" / "file" / "notes1.txt"

file = open(file_path,"w")
file.write("Checking.....")
file.close()

# remove file in os 
# os.remove("/Users/shivam/Documents/Learning/python/advance/file/notes1.txt")



