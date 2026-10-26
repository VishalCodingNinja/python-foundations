"""List, copy, rename, move and delete files, safely.

Everything happens inside a throwaway "playground" folder next to this
script, so none of your real files are touched.
"""
import os
import shutil
from pathlib import Path

playground = Path(__file__).parent / "playground"
shutil.rmtree(playground, ignore_errors=True)   # start fresh every run
os.makedirs(playground)
os.chdir(playground)

# Create a few sample files to work with
for name in ["data.csv", "old.txt", "temp.txt"]:
    with open(name, "w") as f:
        f.write("sample\n")

print(os.listdir("."))               # names in a folder
print(os.path.exists("data.csv"))    # True
os.makedirs("backup", exist_ok=True)
os.makedirs("archive", exist_ok=True)

shutil.copy("data.csv", "backup/")
os.rename("old.txt", "new.txt")
shutil.move("new.txt", "archive/")
os.remove("temp.txt")                # no undo!

print(os.listdir("."))
print(os.listdir("archive"))

# The same ideas with pathlib
p = Path("data.csv")
print(p.name, p.stem, p.suffix, p.exists())   # data.csv data .csv True
