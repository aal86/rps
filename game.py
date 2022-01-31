#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#
#AUTOMATED TESTING (GLOBAL)
#defines global function with two parameters, player one's input and the computer's choice
from email.policy import default


def determine_winner (PlayerOne, ComputerChoice):
    if PlayerOne == ComputerChoice:
        print("Both players selected " + PlayerOne + ". It's a tie!")
        return(None)
    elif PlayerOne == "rock":
        if ComputerChoice == "paper":
            print("Paper beats rock! You lose.")
            return("paper")
        else:
            print("Rock beats scissors! You won!")
            return("rock")
    elif PlayerOne == "paper":
        if ComputerChoice == "rock":
            print("Paper beats rock! You won!")
            return("paper")
        else:
            print("Scissors beats paper! You lose.")
            return("scissors")
    elif PlayerOne == "scissors":
        if ComputerChoice == "rock":
            print("Rock beats scissors! You lose.")
            return("rock")
        else:
            print("Scissors beats paper! You won!")
            return("scissors")

#MAIN
if __name__ == "__main__":

#WELCOME MESSAGE
#import os to enable environment variables
    import os

    from dotenv import load_dotenv
    load_dotenv()

#gets the environment variable 'Player_Name' and if there isn't one, defaults PlayerName to Player One
    PlayerName = os.getenv("Player_Name", default = "Player One")

    print("Welcome " + PlayerName + " to my Rock-Paper-Scissors game...")

# ASK FOR USER INPUT
    PlayerOne = input("Please choose either : 'rock', 'paper', or 'scissors': ")

#makes the user input all lowercase 
    PlayerOne = PlayerOne.lower()

    print("You chose: " + PlayerOne)

# VALIDATIONS
    if PlayerOne != "rock" and PlayerOne != "scissors" and PlayerOne != "paper":
        exit()

# COMPUTER CHOICE
    import random

    PossibleChoices = ("rock", "paper", "scissors")
    ComputerChoice = random.choice(PossibleChoices)
    print("The computer chose: " + ComputerChoice)

# DETERMINE THE WINNER
#calls the global function within the main to determine the winner
    determine_winner(PlayerOne, ComputerChoice)

    # if PlayerOne == ComputerChoice:
    #     print("Both players selected " + PlayerOne + ". It's a tie!")
    # elif PlayerOne == "rock":
    #     if ComputerChoice == "scissors":
    #         print("Rock beats scissors! You win!")
    #     else:
    #         print("Paper beats rock! You lose.")
    # elif PlayerOne == "paper":
    #     if ComputerChoice == "rock":
    #         print("Paper beats rock! You win!")
    #     else:
    #         print("Scissors beats paper! You lose.")
    # elif PlayerOne == "scissors":
    #     if ComputerChoice == "paper":
    #         print("Scissors beats paper! You win!")
    #     else:
    #         print("Rock beats scissors! You lose.")


# FINAL RESULTS
    print("Thanks for playing. Please play again!")


        
    



