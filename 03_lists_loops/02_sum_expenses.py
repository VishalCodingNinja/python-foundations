"""Module 3 · Demo: sum expenses

Adds up a week of spending with a for loop, then checks the answer with
Python's built-in sum().

Run it:  python 03_lists_loops/02_sum_expenses.py
"""

# One expense per day; a long list can continue on the next line
expenses = [10.50, 8.00, 5.00, 15.00,
            20.00, 20.00, 9.00]

# The accumulator pattern: start at 0, add each item inside the loop,
# then use the result after the loop has finished
total = 0
for expense in expenses:
    total += expense  # short for: total = total + expense

print("You spent", total, "this week")           # 87.5
# The average is the total divided by how many items there are
print("Average per day:", total / len(expenses))  # 12.5
# sum() does the whole loop for you in one call
print("Built-in sum():", sum(expenses))           # 87.5
