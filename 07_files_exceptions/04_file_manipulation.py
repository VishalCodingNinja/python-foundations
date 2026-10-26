"""Module 7 · File manipulation

List, copy, rename, move and delete files from code with the os and shutil
modules, then do the same kind of thing with pathlib.

Everything happens inside a throwaway "playground" folder next to this
script, so none of your real files are touched.

Run it:  python 07_files_exceptions/04_file_manipulation.py
"""
import os      # talks to the operating system: folders, renames, deletes
import shutil  # higher-level file tools: copy, move, remove whole folders
from pathlib import Path

playground = Path(__file__).parent / "playground"
shutil.rmtree(playground, ignore_errors=True)   # start fresh every run
os.makedirs(playground)   # create the folder
os.chdir(playground)      # work inside it from now on ("change directory")

# Create a few sample files to work with
for name in ["data.csv", "old.txt", "temp.txt"]:
    with open(name, "w") as f:
        f.write("sample\n")

print(os.listdir("."))               # names in a folder ("." is this folder)
print(os.path.exists("data.csv"))    # True
# exist_ok=True means "don't complain if the folder is already there"
os.makedirs("backup", exist_ok=True)
os.makedirs("archive", exist_ok=True)

shutil.copy("data.csv", "backup/")   # copy: the original stays where it is
os.rename("old.txt", "new.txt")      # rename, in the same folder
shutil.move("new.txt", "archive/")   # move into another folder
os.remove("temp.txt")                # delete: skips the recycle bin, no undo!

print(os.listdir("."))
print(os.listdir("archive"))

# The same ideas with pathlib: a Path object knows the parts of its name
p = Path("data.csv")
print(p.name, p.stem, p.suffix, p.exists())   # data.csv data .csv True
