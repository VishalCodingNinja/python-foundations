expenses = [10.50, 8.00, 5.00, 15.00,
            20.00, 20.00, 9.00]

total = 0
for expense in expenses:
    total += expense  # total = total + expense

print("You spent", total, "this week")           # 87.5
print("Average per day:", total / len(expenses))  # 12.5
print("Built-in sum():", sum(expenses))           # 87.5
