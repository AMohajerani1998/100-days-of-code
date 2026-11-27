import random
print("Let's play Rock Paper Scissors!")
options = ["rock", "paper", "scissors"]
player_input = input("What do you choose? Rock, Paper or Scissors? ").lower()

computer = options[random.randint(0, (len(options) - 1))]
print(f"Computer picked \"{computer}\" | You picked \"{player_input}\"")
if player_input in options:
    if (computer == "rock" and player_input == "paper") or (computer == "paper" and player_input == "rock"):
        if computer == "rock":
            print("you win!")
        else:
            print("you lose")
    elif (computer == "scissors" and player_input == "rock") or (computer == "rock" and player_input == "scissors"):
        if computer == "rock":
            print("you lose")
        else:
            print("you win!")
    elif (computer == "paper" and player_input == "scissors") or (computer == "scissors" and player_input == "paper"):
        if computer == "scissors":
            print("you lose")
        else:
            print("you win!")
    else:
        print("it's a tie...")
else:
    print("Bad input! Choose again...")