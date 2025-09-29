import random

playerWinCount = 0
computerWinCount = 0

print("Welcome top rock paper scissors game!")
playerInput = input("It's your turn! r/p/s \n")
comChoices = {0: "r", 1: "p", 2: "s"}
comTurn = comChoices[random.randint(0,2)]

print("The computer went: " + comTurn)

round = playerInput+comTurn
playerResults = {
    "rr": "d", "rp": "l", "rs": "w",
    "pp": "d", "pr": "w", "ps": "l",
    "ss": "d", "sr": "l", "sp": "w"
    }

playerOutcome = playerResults[round]

if playerOutcome == "w":
    print("You win!")
    playerWinCount+=1
elif playerOutcome == "d":
    print("It's a draw!")
else:
    print("You lose!")
    computerWinCount+=1