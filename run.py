from random import randint

options = ["Rock", "Paper", "Scissors"]
player_option = []


def runGame():

    cpu = options[randint(0,2)]

    player = False

    while player == False:
        print("Welcome to Rock, Paper, Scissors!")
        print('Please select either "Rock", "Paper" or "Scissors"')
        print('To quit the game, type "quit"')
        player = input("Choose Wisely!: ")
        player = player.capitalize()
        player_option.append(player)

        if player == "Quit":
            break

        if validate_option(player_option) == True:
            if player == cpu:
                print("You chose",player,". CPU chose",cpu,".")
                print("Its a TIE!!!\n")
            elif player == "Rock":
                if cpu == "Paper":
                    print("You chose Rock. CPU chose Paper.")
                    print("You lose!\n")
                else:
                    print("You chose Rock. CPU chose Scissors.")
                    print("You win!\n")
            elif player == "Paper":
                if cpu == "Scissors":
                    print("You chose Paper. CPU chose Scissors.")
                    print("You lose!\n")
                else:
                    print("You chose Paper. CPU chose Rock.")
                    print("You win!\n")
            elif player == "Scissors":
                if cpu == "Rock":
                    print("You chose Scissors. CPU chose Rock.")
                    print("You lose!\n")
                else:
                    print("You chose Scissors. CPU chose Paper.")
                    print("You win!\n")

        player = False
        cpu = options[randint(0,2)]


def validate_option(player_option):
    try:
        [option for option in player_option]
        if ("Rock" or "Paper" or "Scissors") not in player_option:
            player_option.clear()
            raise ValueError(
            "Invalid answer. Please try again.\n"
         )

    except ValueError as e:
        print(f"Invalid data: {e}")
        return False
      
  
    return True


def main():
    runGame()

main()