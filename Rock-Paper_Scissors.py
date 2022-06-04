import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = (input("rock, paper, scissors? ")).lower()

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Its a draw!")

    elif player == "rock":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Player win")
        else:
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer Win")

    elif player == "paper":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Player win")
        else:
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer Win")

    elif player == "scissors":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Player win")
        else:
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer Win")
    print()
