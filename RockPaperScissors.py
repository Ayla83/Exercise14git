from random import randint


def user(userinput):
    if userinput == "R":
        userchoice = "Rock"
    elif userinput == "P":
        userchoice = "Paper"
    elif userinput == "S":
        userchoice = "Scissors"
    return userchoice


def computer():
    comprand = randint(0, 2)                # Create a random number for the computer's choice
    if comprand == 0:
        compchoice = "Rock"
    elif comprand == 1:
        compchoice = "Paper"
    elif comprand == 2:
        compchoice = "Scissors"
    return compchoice


def game(userhand, computerhand):
    if userhand == computerhand:
        print("It's a tie!")
    elif userhand == "Rock":
        if computerhand == "Paper":
            print("Paper covers rock,")
            print("Computer wins - you lose!")
            return 1                                # function returns 1 if computer wins, or 2 if user wins
        elif computerhand == "Scissors":
            print("Rock blunts scissors,")
            print("You win!")
            return 2
    elif userhand == "Paper":
        if computerhand == "Scissors":
            print("Scissors cut paper,")
            print("Computer wins - you lose!")
            return 1
        elif computerhand == "Rock":
            print("Paper covers rock,")
            print("You win!")
            return 2
    elif userhand == "Scissors":
        if computerhand == "Rock":
            print("Rock blunts scissors,")
            print("Computer wins - you lose!")
            return 1
        elif computerhand == "Paper":
            print("Scissors cut paper,")
            print("You win!")
            return 2


def outof3(userscore, compscore):
    if userscore == 2 and compscore == 0 or userscore == 2 and compscore == 1:
        print("Best out of 3, you win!")
    elif compscore == 2 and userscore == 0 or compscore == 2 and userscore == 1:
        print("Best out of 3, computer wins!")
    else:
        pass


userscore = 0
compscore = 0

while True:
    userinput = input("Choose Rock (R), Paper (P) or Scissors (S)! ").upper()  # user inputs their choice
    if userinput != "R" and userinput != "P" and userinput != "S":
        print("You didn't choose a hand!  Try again")                   # check user has input a valid option
    else:
        userhand = user(userinput)

        print("You chose: ", userhand)

        computerhand = computer()                        # function to randomly select computer's hand
        print("Computer chose: ", computerhand)

        result = game(userhand, computerhand)            # function to check who wins
        if result == 1:
            compscore += 1
        elif result == 2:
            userscore += 1
        print("User:", userscore, "Computer:", compscore)

        outof3(userscore, compscore)                    # function to check who is winning during first three games

        playagain = input("Play again? Y/N: ").upper()
        if playagain == "N":
            print("Thanks for playing!")
            break
