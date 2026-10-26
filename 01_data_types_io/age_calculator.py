current_year = int(input("Current year: "))
birth_year = int(input("Birth year: "))

age = current_year - birth_year
months = age * 12
days = age * 365

print(f"You are about {age} years old.")
print(f"That's {months} months, or ~{days} days.")
