"""Solution · Exercise 1: tip calculator (Module 1)

Task: exercises/ex01_tip_calculator.py
Run it:  python solutions/ex01_tip_calculator.py
"""

# input() returns text, so convert each answer to a number straight away:
# float() for amounts that can have decimals, int() for a count of people
bill = float(input("Bill total: "))
tip_percent = float(input("Tip %: "))
people = int(input("Split between how many people? "))

# A percentage is "out of 100": 15% of 120 is 120 * 15 / 100 = 18
tip = bill * tip_percent / 100
total = bill + tip
share = total / people

# :.2f shows exactly 2 decimal places, the usual way to show money
print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}")
print(f"Each person pays: {share:.2f}")
