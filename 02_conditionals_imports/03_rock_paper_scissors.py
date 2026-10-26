"""Module 2 · Demo: rock, paper, scissors

A first version of the game: the computer always picks "paper", and
if / elif / else decides who wins.

Run it:  python 02_conditionals_imports/03_rock_paper_scissors.py
"""

# .lower() turns "Rock" or "ROCK" into "rock", so capital letters don't matter
you = input("rock, paper or scissors? ").lower()
cpu = "paper"  # hard-coded for now; the next demo makes it random

# The same choice on both sides is a tie
if you == cpu:
    print("Tie!")
# Each line is one winning pair for you. "and" is checked before "or",
# so every line reads as (you picked X and cpu picked Y).
# The ( ) let the condition continue over several lines.
elif (you == "rock" and cpu == "scissors"
      or you == "paper" and cpu == "rock"
      or you == "scissors" and cpu == "paper"):
    print("You win!")
# Not a tie and not a win, so the computer wins
else:
    print("Computer wins!")
