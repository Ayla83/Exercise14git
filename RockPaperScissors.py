from random import randint

def game(userhand, computerhand):
    if userhand == computerhand:
        print("It's a tie!")
    elif userhand == "rock":
        if computerhand == "paper":
            print("paper covers rock,")
            print("computer wins - you lose!")
            return 1                                # function returns 1 if computer wins, or 2 if user wins
        elif computerhand == "scissors":
            print("rock blunts scissors,")
            print("you win!")
            return 2
    elif userhand == "paper":
        if computerhand == "scissors":
            print("scissors cut paper,")
            print("computer wins - you lose!")
            return 1
        elif computerhand == "rock":
            print("paper covers rock,")
            print("you win!")
            return 2
    elif userhand == "scissors":
        if computerhand == "rock":
            print("rock blunts scissors,")
            print("computer wins - you lose!")
            return 1
        elif computerhand == "paper":
            print("scissors cut paper,")
            print("you win!")
            return 2


userscore = 0
compscore = 0

while True:
    userinput = input("Choose Rock (R), Paper (P) or Scissors (S)! ").upper()  # user inputs their choice
    if userinput == "R":
        userhand = "rock"
    elif userinput == "P":
        userhand = "paper"
    elif userinput == "S":
        userhand = "scissors"
    else:
        print("You didn't choose a hand!  Try again")

    print("You chose: ", userhand)

    comprand = randint(0, 2)                # Create a random number for the computer's choice
    if comprand == 0:
        computerhand = "rock"
    elif comprand == 1:
        computerhand = "paper"
    elif comprand == 2:
        computerhand = "scissors"
    else:
        print("Something went wrong")

    print("Computer chose: ", computerhand)

    result = game(userhand, computerhand)            # check who wins
    if result == 1:
        compscore +=1
    elif result == 2:
        userscore +=1
    print("User:", userscore, "Computer:", compscore)

    playagain = input("Play again? Y/N: ").upper()
    if playagain == "N":
        print("Thanks for playing!")
        break
