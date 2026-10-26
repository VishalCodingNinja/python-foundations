import random

options = ["rock", "paper", "scissors"]
cpu = random.choice(options)

you = input("rock, paper or scissors? ").lower()
print("Computer chose", cpu)

if you not in options:
    print("Invalid choice.")
elif you == cpu:
    print("Tie!")
elif (you == "rock" and cpu == "scissors"
      or you == "paper" and cpu == "rock"
      or you == "scissors" and cpu == "paper"):
    print("You win!")
else:
    print("Computer wins!")
