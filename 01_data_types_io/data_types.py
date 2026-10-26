# Introducing data types: int, float, str and bool

length = 10       # int: a whole number
price = 4.99      # float: a decimal number
name = "Python"   # str: text in quotes
is_fun = True     # bool: True or False

print(type(length))   # <class 'int'>
print(type(price))    # <class 'float'>
print(type(name))     # <class 'str'>
print(type(is_fun))   # <class 'bool'>

# "10" (a str) is not the same as 10 (an int)
print(type("10"))     # <class 'str'>

# Floats are approximate, so round them for display
print(price * 10)            # 49.900000000000006
print(round(price * 10, 2))  # 49.9
