from pathlib import Path

# notes.txt sits next to this script, wherever you run it from
notes = Path(__file__).parent / "notes.txt"

with open(notes, encoding="utf-8") as f:
    text = f.read()            # whole file, one str
print(text)

with open(notes, encoding="utf-8") as f:
    for line in f:             # one line at a time
        print(line.strip())

with open(notes, encoding="utf-8") as f:
    lines = f.readlines()      # a list of lines
print(len(lines), "lines")

try:
    with open("does_not_exist.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("No such file, but the program keeps running.")
