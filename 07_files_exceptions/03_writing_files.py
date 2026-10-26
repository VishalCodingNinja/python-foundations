"""Module 7 · Demo: writing files

Writes a shopping list to list.txt, adds one more item, then reads the
file back. The second argument to open() is the mode.

Run it:  python 07_files_exceptions/03_writing_files.py
"""

from pathlib import Path

shopping = ["milk", "eggs", "bread"]
list_file = Path(__file__).parent / "list.txt"

# "w" (write) creates the file, or wipes it first if it already exists
with open(list_file, "w", encoding="utf-8") as f:  # overwrite
    for item in shopping:
        # write() doesn't add a line break, so add "\n" yourself
        f.write(item + "\n")

# "a" (append) keeps what's already there and adds to the end
with open(list_file, "a", encoding="utf-8") as f:  # add to the end
    f.write("coffee\n")

# With no mode, open() uses "r" (read), the default
with open(list_file, encoding="utf-8") as f:
    print(f.read())
