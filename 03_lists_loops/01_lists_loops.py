expenses = [12.50, 40.00, 7.25]

print(expenses[0])     # 12.5, the first item
print(expenses[-1])    # 7.25, the last item
print(len(expenses))   # 3

expenses.append(20)     # add to the end
expenses.remove(40.00)  # remove by value
print(expenses)         # [12.5, 7.25, 20]

for amount in expenses:
    print(amount)
