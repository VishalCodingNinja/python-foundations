"""Module 1 · Strings and input and output

input() asks the user a question and print() shows the answer. This file
also shows how to turn typed text into a number, and how to build text
with + and with f-strings.

Run it:  python 01_data_types_io/03_strings_input_output.py
"""

# input() shows the prompt, waits for the user to type and press Enter,
# then gives back what they typed
name = input("What's your name? ")
age = input("How old are you? ")

# input() always gives back a str, even when the user types digits.
# int() converts text like "30" into the number 30 so we can do maths.
age = int(age)

# + joins (concatenates) strings together
print("Hi " + name + "!")
# An f-string (f before the quote) puts the value of anything inside { }
# straight into the text, even a calculation like age + 1
print(f"Next year you'll be {age + 1}.")
# .upper() gives an UPPERCASE copy; len() counts the characters
print(name.upper(), len(name))
