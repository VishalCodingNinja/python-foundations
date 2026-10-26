"""Module 1 · Demo: tax calculator

Uses variables and arithmetic to work out the tax on a price and the total
to pay.

Run it:  python 01_data_types_io/02_tax_calculator.py
"""

price = 59.99
tax_rate = 0.08  # 8% written as a decimal: 8 / 100 = 0.08

# The tax is a percentage of the price, so multiply the two
tax = price * tax_rate
# The customer pays the price plus the tax
total = price + tax

# round(value, 2) keeps 2 decimal places, like money
print("Tax:", round(tax, 2))      # Tax: 4.8
print("Total:", round(total, 2))  # Total: 64.79

# Try it: change price and tax_rate, then run the file again
