"""Solution · Exercise 5: temperature converter (Module 5)

Task: exercises/ex05_temperature_converter.py
Run it:  python solutions/ex05_temperature_converter.py
"""


# Each of these functions does one conversion and returns the result
def c_to_f(celsius):
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# unit="C" is a default, so convert(100) means 100 degrees Celsius
def convert(value, unit="C"):
    """Convert value to the other scale and describe the result."""
    if unit == "C":
        return f"{value}°C = {c_to_f(value):.1f}°F"
    # Any other unit is treated as Fahrenheit
    return f"{value}°F = {f_to_c(value):.1f}°C"


value = float(input("Temperature: "))
unit = input("Unit (C or F): ").upper()  # .upper() accepts "c" as well as "C"
print(convert(value, unit))
