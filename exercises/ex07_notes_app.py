"""Exercise 7: Notes app  (Module 7: files and exceptions)

Write a small menu program that keeps notes in a text file:
  1) Add   asks for a note and appends it to my_notes.txt
  2) Show  prints every saved note with a number in front;
           if the file doesn't exist yet, print "No notes yet."
  3) Quit  ends the program
Anything else, including letters, prints "Please type 1, 2 or 3."

Sample run:
    1) Add  2) Show  3) Quit: 2
    No notes yet.
    1) Add  2) Show  3) Quit: 1
    Note: Buy milk
    Saved.
    1) Add  2) Show  3) Quit: 2
    1. Buy milk
    1) Add  2) Show  3) Quit: x
    Please type 1, 2 or 3.
    1) Add  2) Show  3) Quit: 3

Hint: open(..., "a") appends; catch FileNotFoundError when reading.
Hint: int("x") raises ValueError, so wrap it in try / except.
Hint: while True: ... break  keeps the menu running until Quit.
Solution: solutions/ex07_notes_app.py
"""

# TODO 1: write add_note() and show_notes() functions

# TODO 2: write the menu loop with try / except ValueError
