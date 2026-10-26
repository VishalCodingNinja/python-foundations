"""Module 7 · Demo: file organization

Sorts the files in a folder into sub-folders by file type: every .pdf goes
into pdf_files/, every .jpg into jpg_files/, and so on.

By default it works on a demo folder, messy_folder, which it creates for
you. Point FOLDER at a real folder only after trying it on a copy: the
moves are real.

Run it:  python 07_files_exceptions/05_file_organizer.py
"""
import os
import shutil
from pathlib import Path

# CAPITAL names are a convention for settings you might want to change
FOLDER = Path(__file__).parent / "messy_folder"


# Make the demo folder, with a few empty files of different types
def make_demo_files(folder):
    os.makedirs(folder, exist_ok=True)
    for name in ["cv.pdf", "scan.pdf", "photo.jpg", "notes.txt", "README"]:
        open(os.path.join(folder, name), "w").close()  # creates an empty file


if not os.path.exists(FOLDER):
    make_demo_files(FOLDER)

folder = FOLDER
for name in os.listdir(folder):
    path = os.path.join(folder, name)  # folder + name = the full path
    if not os.path.isfile(path):
        continue  # skip folders: continue jumps straight to the next name
    # splitext("cv.pdf") gives ("cv", ".pdf"), and [1] takes the extension.
    # A file with no extension (like README) gets ".none" instead.
    ext = os.path.splitext(name)[1].lower() or ".none"
    # ext[1:] drops the dot (".pdf" becomes "pdf"), so the folder is pdf_files
    target = os.path.join(folder, ext[1:] + "_files")
    os.makedirs(target, exist_ok=True)
    shutil.move(path, target)
    print(f"{name} -> {os.path.basename(target)}/")
