from random import randint

options = ["Rock", "Paper", "Scissors"]
player_option = []

def runGame():

    cpu = options[randint(0,2)]

    player = False

    while player == False:
        print("Welcome to Rock, Paper, Scissors!")
        print('Please select either "Rock", "Paper" or "Scissors"')
        player = input("Choose Wisely!: ")
        player_option.append(player)

        if player == cpu:
            print("You chose",player,". CPU chose",cpu,".")
            print("Its a TIE!!!")
        elif player == "Rock":
            if cpu == "Paper":
                print("You chose Rock. CPU chose Paper.")
                print("You lose!")
            else:
                print("You chose Rock. CPU chose Scissors.")
                print("You win!")
        elif player == "Paper":
            if cpu == "Scissors":
                print("You chose Paper. CPU chose Scissors.")
                print("You lose!")
            else:
                print("You chose Paper. CPU chose Rock.")
                print("You win!")
        elif player == "Scissors":
            if cpu == "Rock":
                print("You chose Scissors. CPU chose Rock.")
                print("You lose!")
            else:
                print("You chose Scissors. CPU chose Paper.")
                print("You win!")

def main():
    runGame()

main()