import random

player_win_count = 0
computer_win_count = 0
has_quit = False


print("Welcome to our Rock Paper Scissors game!")
print("Press q to quit")


while not has_quit:
    player_input = input("it's your turn! rock/paper/scissors \n").lower()
    if player_input != "scissors" and player_input != "paper" and player_input != "rock":

        print("you must enter rock, paper or scissors!")
        continue
    elif player_input == "q":
        has_quit = True



    com_choices = {0: "rock", 1: "paper", 2: "scissors"}
    com_turn = com_choices[random.randint(0,2)]

    print("the computer chose: " + com_turn)

    # compares player and computer choices
    round = player_input+com_turn
    player_results = {
        "rockrock": "d", "rockpaper": "l", "rockscissors": "w",
        "paperpaper": "d", "paperrock": "w", "paperscissors": "l",
        "scissorsscissors": "d", "scissorrock": "l", "scissorspaper": "w"
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

    print(f"player {player_win_count} : {computer_win_count} computer")

print(f"player {player_win_count} : {computer_win_count} computer")