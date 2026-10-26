"""Sort the files in a folder into sub-folders by file type.

By default it works on a demo folder, messy_folder, which it creates for
you. Point FOLDER at a real folder only after trying it on a copy: the
moves are real.
"""
import os
import shutil
from pathlib import Path

FOLDER = Path(__file__).parent / "messy_folder"


def make_demo_files(folder):
    os.makedirs(folder, exist_ok=True)
    for name in ["cv.pdf", "scan.pdf", "photo.jpg", "notes.txt", "README"]:
        open(os.path.join(folder, name), "w").close()


if not os.path.exists(FOLDER):
    make_demo_files(FOLDER)

folder = FOLDER
for name in os.listdir(folder):
    path = os.path.join(folder, name)
    if not os.path.isfile(path):
        continue  # skip folders
    ext = os.path.splitext(name)[1].lower() or ".none"
    target = os.path.join(folder, ext[1:] + "_files")
    os.makedirs(target, exist_ok=True)
    shutil.move(path, target)
    print(f"{name} -> {os.path.basename(target)}/")
