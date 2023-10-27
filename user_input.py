
import sys
import random
from enum import Enum

computerwin = 0
playerwin = 0
while True:

    playerchoice = input(
        "Enter... \n1 for Rock,\n2 for Paper,\n3 for Scissor:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 2:
        sys.exit("Enter 1, 2 or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("")
    print("you chose " + playerchoice+".")
    print("Python chose " + computerchoice + ".")
    print("")

    if player == 1 and computer == 3:
        playerwin += 1
        print("you win for " + str(playerwin) + " times !")
    elif player == 2 and computer == 1:
        playerwin += 1
        print("you win for " + str(playerwin) + " times !")
    elif player == 3 and computer == 2:
        playerwin += 1
        print("you win for " + str(playerwin) + " times !")
    elif player == computer:
        print("Tie Game!")
    else:
        computerwin += 1
        print("🐍python wins for " + str(computerwin) + " times !")
