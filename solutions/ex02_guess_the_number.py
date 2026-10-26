"""Solution · Exercise 2: guess the number (Module 2)

Task: exercises/ex02_guess_the_number.py
Run it:  python solutions/ex02_guess_the_number.py
"""

import random

# randint(1, 10) can return any whole number from 1 to 10, both included
secret = random.randint(1, 10)
guess = int(input("Guess a number from 1 to 10: "))

# Check the bonus case first. 1 <= guess <= 10 is True only inside the
# range, and not flips it, so this branch catches guesses outside 1 to 10.
if not 1 <= guess <= 10:
    print("Out of range. Pick 1 to 10 next time.")
elif guess == secret:
    print("Correct!")
# Only one branch ever runs, so each wrong-guess message reveals the number
elif guess < secret:
    print(f"Too low. It was {secret}.")
else:
    print(f"Too high. It was {secret}.")
