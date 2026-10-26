from pathlib import Path

NOTES_FILE = Path(__file__).parent / "my_notes.txt"


def add_note():
    note = input("Note: ")
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(note + "\n")
    print("Saved.")


def show_notes():
    try:
        with open(NOTES_FILE, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No notes yet.")
        return
    # enumerate() counts for you: 1, 2, 3, ...
    for number, line in enumerate(lines, start=1):
        print(f"{number}. {line.strip()}")


while True:
    try:
        choice = int(input("1) Add  2) Show  3) Quit: "))
    except ValueError:
        print("Please type 1, 2 or 3.")
        continue
    if choice == 1:
        add_note()
    elif choice == 2:
        show_notes()
    elif choice == 3:
        break
    else:
        print("Please type 1, 2 or 3.")
