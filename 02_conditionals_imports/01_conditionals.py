"""Module 2 · Conditionals

if / elif / else lets a program choose what to do. Python checks each
condition from top to bottom and runs only the first block that is True.

Run it:  python 02_conditionals_imports/01_conditionals.py
"""

temp = int(input("Temperature in °C: "))

# The colon : starts a block; the indented lines below it belong to it
if temp >= 30:
    print("Hot. Drink water.")
# elif ("else if") is only checked when every condition above was False
elif temp >= 15:
    print("Nice weather.")
# else runs when none of the conditions above were True
else:
    print("Bring a jacket.")

print("Done.")  # not indented, so it is outside the if and runs every time
