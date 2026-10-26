"""Module 2 · Demo: randomize rock, paper, scissors

The same game as before, but now the computer picks at random with the
random module, and invalid choices are caught.

Run it:  python 02_conditionals_imports/05_rock_paper_scissors_random.py
"""

import random

# A list of the three valid moves
options = ["rock", "paper", "scissors"]
# random.choice() picks one item from the list, different on each run
cpu = random.choice(options)

you = input("rock, paper or scissors? ").lower()
print("Computer chose", cpu)

# "not in" is True when the player's move isn't one of the valid options
if you not in options:
    print("Invalid choice.")
elif you == cpu:
    print("Tie!")
# The three winning pairs for the player, as in the previous demo
elif (you == "rock" and cpu == "scissors"
      or you == "paper" and cpu == "rock"
      or you == "scissors" and cpu == "paper"):
    print("You win!")
else:
    print("Computer wins!")
