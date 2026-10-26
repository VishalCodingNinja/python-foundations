"""Module 7 · Exceptions

When something goes wrong, Python raises an exception and the program
stops. try / except catches it, so the program can respond instead.

Run it:  python 07_files_exceptions/01_exceptions.py
"""

# Code that might fail goes inside try
try:
    age = int(input("Age: "))  # ValueError if you type something like "abc"
    per_year = 1000 / age      # ZeroDivisionError if age is 0
# Each except handles one kind of error
except ValueError:
    print("Please type a whole number.")
except ZeroDivisionError:
    print("Age can't be zero.")
# else runs only when nothing inside try failed
else:
    print(f"{per_year:.1f} per year")
# finally runs every time, error or not, which makes it good for clean-up
finally:
    print("Thanks!")
