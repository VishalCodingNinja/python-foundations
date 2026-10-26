"""Module 7 · Reading files

Three ways to read a text file with open(), and how to handle a file that
doesn't exist.

Run it:  python 07_files_exceptions/02_reading_files.py
"""

from pathlib import Path

# notes.txt sits next to this script, wherever you run it from:
# Path(__file__).parent is this script's folder, and / adds a file name
notes = Path(__file__).parent / "notes.txt"

# with open(...) as f opens the file as f and closes it again automatically,
# even if an error happens inside the block.
# encoding="utf-8" makes sure accents and emoji are read correctly.
with open(notes, encoding="utf-8") as f:
    text = f.read()            # the whole file as one str
print(text)

with open(notes, encoding="utf-8") as f:
    for line in f:             # one line at a time, good for big files
        print(line.strip())    # strip() removes the line break at the end

with open(notes, encoding="utf-8") as f:
    lines = f.readlines()      # a list with one str per line
print(len(lines), "lines")

# Opening a file that doesn't exist raises FileNotFoundError; catch it
try:
    with open("does_not_exist.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("No such file, but the program keeps running.")
