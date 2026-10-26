"""Module 3 · Demo: loan payment calculator

Simulates paying off a loan month by month: each month interest is added
and a fixed payment is taken off, until nothing is owed.

Run it:  python 03_lists_loops/04_loan_calculator.py
"""

balance = 1000.00  # how much is still owed
rate = 0.02        # 2% interest per month
payment = 100.00   # paid back every month

# Try up to 24 months; break stops the loop early once the loan is paid off
for month in range(1, 25):
    # Add one month of interest, then subtract this month's payment
    balance = balance * (1 + rate) - payment
    if balance <= 0:
        print(f"Paid off in month {month}!")
        break  # leave the loop right away
    # :.2f formats the number with exactly 2 decimal places
    print(f"Month {month}: ${balance:.2f} left")
