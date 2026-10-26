def greet(name, greeting="Hello"):
    """Return a friendly greeting."""
    message = f"{greeting}, {name}!"
    return message


print(greet("Ana"))                         # Hello, Ana!
print(greet("Raj", "Hi"))                   # Hi, Raj!
print(greet(greeting="Hey", name="Li"))     # Hey, Li!

# A function with no return gives back None
def say_hi():
    print("hi")


result = say_hi()
print(result)   # None

# message only exists inside greet(), so this line would fail:
# print(message)   # NameError
