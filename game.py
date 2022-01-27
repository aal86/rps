


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#
#WELCOME MESSAGE
import os

PlayerName = os.getenv('Player_Name', default = "Player One")

print("Welcome " + PlayerName + " to my Rock-Paper-Scissors game...")

# ASK FOR USER INPUT
PlayerOne = input("Please choose either : 'rock', 'paper', or 'scissors': ")

print("You chose: " + PlayerOne)

# VALIDATIONS

if PlayerOne != ("ROCK" or "Rock" or "rock" or "SCISSCORS" or "Scissors" or "scissors" or "PAPER" or "Paper" or "paper"):
    exit()

# COMPUTER CHOICE
import random

PossibleChoices = ("rock", "paper", "scissors")
ComputerChoice = random.choice(PossibleChoices)
print("The computer chose: " + ComputerChoice)

# DETERMINE THE WINNER

if PlayerOne == ComputerChoice:
    print("Both players selected " + PlayerOne + ". It's a tie!")
elif PlayerOne == "rock":
    if ComputerChoice == "scissors":
        print("Rock beats scissors! You win!")
    else:
        print("Paper beats rock! You lose.")
elif PlayerOne == "paper":
    if ComputerChoice == "rock":
        print("Paper beats rock! You win!")
    else:
        print("Scissors beats paper! You lose.")
elif PlayerOne == "scissors":
    if ComputerChoice == "paper":
        print("Scissors beats paper! You win!")
    else:
        print("Rock beats scissors! You lose.")


# FINAL RESULTS
print("Thanks for playing. Please play again!")

#AUTOMATED TESTING
def determine_winner (choice_1, choice_2):
    PlayerOne = choice_1
    ComputerChoice = choice_2
    



