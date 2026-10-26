"""Module 1 · Demo: age calculator

Reads two years from the user, converts them to numbers and works out an
approximate age in years, months and days.

Run it:  python 01_data_types_io/04_age_calculator.py
"""

# Wrap input() in int() to turn the typed text into a whole number.
# Without int(), current_year - birth_year would fail with a TypeError,
# because Python can't subtract one str from another.
current_year = int(input("Current year: "))
birth_year = int(input("Birth year: "))

age = current_year - birth_year
months = age * 12
days = age * 365  # approximate: ignores leap years and exact birthdays

# f-strings drop each variable's value into the sentence
print(f"You are about {age} years old.")
print(f"That's {months} months, or ~{days} days.")
