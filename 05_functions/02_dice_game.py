import random


def roll_die(sides=6):
    return random.randint(1, sides)


def play_round(player):
    total = roll_die() + roll_die()
    print(f"{player} rolled {total}")
    return total


you = play_round("You")
cpu = play_round("CPU")

if you > cpu:
    print("You win!")
elif you < cpu:
    print("CPU wins!")
else:
    print("Draw.")
