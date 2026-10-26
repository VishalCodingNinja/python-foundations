"""Module 2 · Conditional operators and booleans

A comparison asks a yes/no question, and the answer is a bool: True or
False. Logical operators (and, or, not) combine those answers.

Run it:  python 02_conditionals_imports/02_operators_booleans.py
"""

# Comparison operators answer True or False
print(5 == 5)   # True:  == means "is equal to"
print(5 != 3)   # True:  != means "is not equal to"
print(2 < 1)    # False: <  means "is less than"
print(9 > 4)    # True:  >  means "is greater than"
print(3 <= 3)   # True:  <= means "is less than or equal to"
print(2 >= 4)   # False: >= means "is greater than or equal to"

# Logical operators combine comparisons
age = 20
has_id = True
day = "Sun"
is_raining = False

print(age >= 18 and has_id)          # True: and needs BOTH sides to be True
print(day == "Sat" or day == "Sun")  # True: or needs at least ONE side True
print(not is_raining)                # True: not flips True to False and back

# Watch out: = assigns a value, == compares two values
x = 5           # store 5 in x
print(x == 5)   # True: asks whether x is equal to 5
