# tax_calculator.py
price = 59.99
tax_rate = 0.08  # 8%

tax = price * tax_rate
total = price + tax

print("Tax:", round(tax, 2))      # Tax: 4.8
print("Total:", round(total, 2))  # Total: 64.79
