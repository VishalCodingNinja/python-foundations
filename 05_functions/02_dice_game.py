"""Module 5 · Demo: dice rolling game with functions

The game is built from two small functions: one rolls a die, the other
plays a round. Each function does one job, so each is easy to change.

Run it:  python 05_functions/02_dice_game.py
"""

import random


# Roll one die. sides=6 is a default, so roll_die() is a normal die;
# change it to 20 and every roll in the game uses a 20-sided die.
def roll_die(sides=6):
    return random.randint(1, sides)


# Roll two dice for a player, show the result and return the total
def play_round(player):
    total = roll_die() + roll_die()
    print(f"{player} rolled {total}")
    return total


# Each call plays a whole round and gives back that player's total
you = play_round("You")
cpu = play_round("CPU")

# Compare the two totals to find the winner
if you > cpu:
    print("You win!")
elif you < cpu:
    print("CPU wins!")
else:
    print("Draw.")
