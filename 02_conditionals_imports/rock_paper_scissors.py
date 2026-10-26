you = input("rock, paper or scissors? ").lower()
cpu = "paper"  # hard-coded for now

if you == cpu:
    print("Tie!")
elif (you == "rock" and cpu == "scissors"
      or you == "paper" and cpu == "rock"
      or you == "scissors" and cpu == "paper"):
    print("You win!")
else:
    print("Computer wins!")
