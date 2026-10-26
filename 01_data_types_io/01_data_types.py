"""Module 1 · Introducing data types

Every value in Python has a type, and the type decides what you can do with
it. This file shows the four basic types and how to check them.

Run it:  python 01_data_types_io/01_data_types.py
"""

# A variable is a name that points to a value. The = sign stores the value
# on the right under the name on the left.
length = 10       # int: a whole number, no decimal point
price = 4.99      # float: a number with a decimal point
name = "Python"   # str: text, always inside quotes
is_fun = True     # bool: only True or False (capital T and F)

# type() tells you which type a value is
print(type(length))   # <class 'int'>
print(type(price))    # <class 'float'>
print(type(name))     # <class 'str'>
print(type(is_fun))   # <class 'bool'>

# Quotes make anything a str: "10" is text, not the number 10,
# so you can't do maths with it until you convert it with int("10")
print(type("10"))     # <class 'str'>

# Floats are stored in binary, so some decimals can't be stored exactly.
# That's why 4.99 * 10 prints a tiny error at the end.
print(price * 10)            # 49.900000000000006
# round(value, digits) tidies the number up for display
print(round(price * 10, 2))  # 49.9
