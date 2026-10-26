balance = 1000.00
rate = 0.02  # 2% interest per month
payment = 100.00

for month in range(1, 25):
    balance = balance * (1 + rate) - payment
    if balance <= 0:
        print(f"Paid off in month {month}!")
        break
    print(f"Month {month}: ${balance:.2f} left")
