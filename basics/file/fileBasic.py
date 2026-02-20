# file in read mode

from pathlib import Path

base_dir = Path.cwd()   # current working directory
file_path = base_dir / "basics" / "file" / "notes.txt"
file = open(file_path,"r")
data = file.read()
file.close()

print(data)
print("shivam" in data.lower())




