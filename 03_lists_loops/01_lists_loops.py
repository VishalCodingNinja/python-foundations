"""Module 3 · Lists and loops

A list stores many values in order. A for loop runs the same code once for
every item in a list.

Run it:  python 03_lists_loops/01_lists_loops.py
"""

# Square brackets make a list; items are separated by commas
expenses = [12.50, 40.00, 7.25]

# Each item has a position, called its index. Counting starts at 0, not 1.
print(expenses[0])     # 12.5, the first item
# Negative indexes count back from the end: -1 is the last item
print(expenses[-1])    # 7.25, the last item
# len() gives the number of items
print(len(expenses))   # 3

# Lists can change after you create them
expenses.append(20)     # add 20 to the end
expenses.remove(40.00)  # remove the first item equal to 40.0
print(expenses)         # [12.5, 7.25, 20]

# The loop variable (amount) holds each item in turn: 12.5, then 7.25, then 20
for amount in expenses:
    print(amount)
