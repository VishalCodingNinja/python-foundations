name = input("What's your name? ")
age = input("How old are you? ")

# input() always gives back a str
age = int(age)

print("Hi " + name + "!")
print(f"Next year you'll be {age + 1}.")
print(name.upper(), len(name))
