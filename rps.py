import random

player_win_count = 0
computer_win_count = 0


print("welcome top rock paper scissors game!")

while player_win_count < 2 and computer_win_count < 2:
    player_input = input("it's your turn! r/p/s \n")
    if(player_input != "s" and player_input != "p" and player_input != "r"):
        print("you must enter r, p or s!")
        continue

    com_choices = {0: "r", 1: "p", 2: "s"}
    com_turn = com_choices[random.randint(0,2)]

    print("the computer went: " + com_turn)

    # compares player and computer choices
    round = player_input+com_turn
    player_results = {
        "rr": "d", "rp": "l", "rs": "w",
        "pp": "d", "pr": "w", "ps": "l",
        "ss": "d", "sr": "l", "sp": "w"
        }

    player_outcome = player_results[round]

    if player_outcome == "w":
        print("you won this round!")
        player_win_count+=1
    elif player_outcome == "d":
        print("it's a draw!")
    else:
        print("you lost this round!")
        computer_win_count+=1

if player_win_count == 2:
    print("you won!!!!!")
else:
    print("computer won!")