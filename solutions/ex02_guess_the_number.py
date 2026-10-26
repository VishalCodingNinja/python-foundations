import random

secret = random.randint(1, 10)
guess = int(input("Guess a number from 1 to 10: "))

if not 1 <= guess <= 10:
    print("Out of range. Pick 1 to 10 next time.")
elif guess == secret:
    print("Correct!")
elif guess < secret:
    print(f"Too low. It was {secret}.")
else:
    print(f"Too high. It was {secret}.")
