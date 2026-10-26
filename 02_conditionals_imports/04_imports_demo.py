"""Module 2 · Importing modules

A module is a file of ready-made code. Python ships with hundreds of them
(the standard library), and import makes one available in your program.

Run it:  python 02_conditionals_imports/04_imports_demo.py
"""

# import module_name, then call module_name.function()
import random
print(random.randint(1, 6))     # a random whole number from 1 to 6, inclusive

import math
print(math.sqrt(81))            # square root: 9.0

# from module import name lets you use the name directly, without "datetime."
from datetime import date
print(date.today().year)        # the current year, e.g. 2026

# as gives a module a shorter nickname
import statistics as stats
print(stats.mean([3, 5, 10]))   # the average of the list: 6

# Normally all imports go at the top of the file.
# They are spread out here so each one sits next to its example.
