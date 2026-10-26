from pathlib import Path

shopping = ["milk", "eggs", "bread"]
list_file = Path(__file__).parent / "list.txt"

with open(list_file, "w", encoding="utf-8") as f:  # overwrite
    for item in shopping:
        f.write(item + "\n")

with open(list_file, "a", encoding="utf-8") as f:  # add to the end
    f.write("coffee\n")

with open(list_file, encoding="utf-8") as f:
    print(f.read())
