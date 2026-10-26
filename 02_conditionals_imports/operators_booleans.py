# Comparison operators answer True or False
print(5 == 5)   # True
print(5 != 3)   # True
print(2 < 1)    # False
print(9 > 4)    # True
print(3 <= 3)   # True
print(2 >= 4)   # False

# Logical operators combine comparisons
age = 20
has_id = True
day = "Sun"
is_raining = False

print(age >= 18 and has_id)          # True: both sides are True
print(day == "Sat" or day == "Sun")  # True: one side is True
print(not is_raining)                # True: not flips False

# = assigns a value, == compares two values
x = 5
print(x == 5)   # True
