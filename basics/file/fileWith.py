# with keyword auto close

from pathlib import Path

try:
  base_dir = Path.cwd()   # current working directory
  file_path = base_dir / "basics" / "file" / "notes.txt"
  with  open(file_path,"r") as file2:
    line1 = file2.readlines()
    print(len(line1))
    line2 = file2.readline() # read single line 
    line3 = file2.read() # read data in file
    print(line1)
    print(line2)
    print(line3)
except FileNotFoundError:
  print("File Not Found")    
