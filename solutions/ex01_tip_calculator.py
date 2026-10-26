bill = float(input("Bill total: "))
tip_percent = float(input("Tip %: "))
people = int(input("Split between how many people? "))

tip = bill * tip_percent / 100
total = bill + tip
share = total / people

print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}")
print(f"Each person pays: {share:.2f}")
