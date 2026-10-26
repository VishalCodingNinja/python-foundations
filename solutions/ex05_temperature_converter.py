def c_to_f(celsius):
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert(value, unit="C"):
    """Convert value to the other scale and describe the result."""
    if unit == "C":
        return f"{value}°C = {c_to_f(value):.1f}°F"
    return f"{value}°F = {f_to_c(value):.1f}°C"


value = float(input("Temperature: "))
unit = input("Unit (C or F): ").upper()
print(convert(value, unit))
