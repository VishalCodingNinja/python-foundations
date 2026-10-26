try:
    age = int(input("Age: "))
    per_year = 1000 / age
except ValueError:
    print("Please type a whole number.")
except ZeroDivisionError:
    print("Age can't be zero.")
else:
    print(f"{per_year:.1f} per year")
finally:
    print("Thanks!")
