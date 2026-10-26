"""Solution · Exercise 7: notes app (Module 7)

Task: exercises/ex07_notes_app.py
Run it:  python solutions/ex07_notes_app.py
"""

from pathlib import Path

# The notes file lives next to this script
NOTES_FILE = Path(__file__).parent / "my_notes.txt"


def add_note():
    note = input("Note: ")
    # "a" (append) adds to the end, and creates the file the first time
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(note + "\n")
    print("Saved.")


def show_notes():
    # Until the first note is added, the file doesn't exist yet
    try:
        with open(NOTES_FILE, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No notes yet.")
        return  # leave the function early
    # enumerate() counts for you: 1, 2, 3, ...
    for number, line in enumerate(lines, start=1):
        print(f"{number}. {line.strip()}")


# while True repeats forever, until break leaves the loop
while True:
    try:
        choice = int(input("1) Add  2) Show  3) Quit: "))
    except ValueError:
        # int() failed, so the user typed something that isn't a number
        print("Please type 1, 2 or 3.")
        continue  # go back to the top of the loop and ask again
    if choice == 1:
        add_note()
    elif choice == 2:
        show_notes()
    elif choice == 3:
        break
    else:
        # A number, but not one of the menu options
        print("Please type 1, 2 or 3.")
