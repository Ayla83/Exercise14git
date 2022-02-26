# User will play against computer
# Design a program which:
# Prompts the user to enter a value R, P, or S
# Program should convert this value into Rock, Paper or Scissors respectively
# Ask the computer to generate a random value between 0 and 2
# Convert the computer's choice: 0 becomes Rock, 1 becomes Paper, 2 becomes Scissors'
# Compare user's choice with computer's choice to display a message indicating whether the user won, lost or drew
# against computer

# Showcase what you have learned about conditional statements and create your own functions

# Still to do: add in conditionals and functions

from random import randint

# user inputs their choice
userinput = input("Choose Rock (R), Paper(P) or Scissors(S)! ").upper()

# reassign choice of letter to game object
if userinput == "R":
    userhand = "rock"
elif userinput == "P":
    userhand = "paper"
elif userinput == "S":
    userhand = "scissors"
else:
    print("You didn't choose a hand!  Try again")

print("userhand is: ", userhand)

# Create a random number for the computer's choice
comprand = randint(0,2)

if comprand == 0:
    computerhand = "rock"
elif comprand == 1:
    computerhand = "paper"
elif comprand == 2:
    computerhand = "scissors"
else:
    print("Something went wrong")

print("computerhand is: ", computerhand)

# Put together the two opponents in a set
gamelist = {userhand, computerhand}

print("The game is: ", gamelist)

# Define the general sets of play
rockpaper = {"rock", "paper"}
paperscissors = {"paper", "scissors"}
scissorsrock = {"scissors", "rock"}

# big loop for checking who wins
if gamelist == rockpaper:
    for item in gamelist:
        if item == "paper":                 # rock v paper, paper wins
            print(item, "covers rock,")
            if item == userhand:            # print who won
                print("user wins!")
            elif item == computerhand:
                print("computer wins")
            else:
                print("something wrong 1")
        else:
            pass
elif gamelist == paperscissors:
    for item in gamelist:
        if item == "scissors":              # paper v scissors, scissors wins
            print(item, "cut paper,")
            if item == userhand:            # print who won
                print("user wins!")
            elif item == computerhand:
                print("computer wins")
            else:
                print("something wrong 2")
        else:
            pass
elif gamelist == scissorsrock:
    for item in gamelist:
        if item == "rock":                  # scissors v rock, rock wins
            print(item, "blunts scissors,")
            if item == userhand:            # print who won
                print("user wins!")
            elif item == computerhand:
                print("computer wins")
            else:
                print("something wrong 3")
        else:
            pass
elif len(gamelist)==1:                      # if userhand = computerhand, it's a tie
    print("It's a tie!  Try again?")
else:
     print("Something else went wrong")




# Compare to other class members:
# Have we achieved this differently?
# Does anyone's solution stand out?
# How would you structure your code differently?
# Would you consider changing the names of my variables or functions?


