# rps-starter

A Starter Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

## Setup

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```
    first time only

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Requirements

Asks for the user input using the input function while giving the user the options between rock, paper, or scissors

Uses the .lower() function to make the user's input lowercase to avoid case sensitive testing 

Uses the print function to print the user's input

Uses an if statement to validate that the user's input is either rock, scissors, or paper and if it is false exits the program

Imports the random module

Creates a list of valid choices and passes them to the random choice function

Uses the print function to print the computer's input

Calls the global function determine_winner(PlayerOne, ComputerChoice) to determine the winter and print the outputs of the game

Uses the print function to thank the user for playing and welcomes them to play again

## Further Exploration
Install the package 

    ```sh
    pip install python-dotenv
    ```
Create an .env file and defines the Player_Name variable where the user must input their own name under this file so the game.py file can read it
    For example: Player_Name = "Abby" defines the environment variable to the name Abby

Within the requirements.txt must add python-dotenv to allow the environment variables to work

Import the os module to enable environment variables in the game.py file

Add the lines below into the game.py file to access and use the environment variables
    from dotenv import load_dotenv
    load_dotenv()

Define the player's name in the game.py file using os.getenv passing the environment variable creating in the .env file followed by a comma and setting the default player's name to Player One

Uses the print function to welcome the player to the game using the environment variable to print the player's name as well

Defines the function determine_winner globally with two parameters, player one's input and the computer's choice

determine_winner function has mutliple conditional statements to test all nine possibilities and prints and returns the results

Creates the main to seperate the global function from the main 

Add another file called game_test.py which tests the nine possible outcome and contains the line below to access the function in the game.py file
    from game import determine_winner

Install the pytest package
    ```sh
    pip install pytest
    ```

Add 'pytest' to the requirements.txt to ensure pytest package has been installed into the active virtual environment

## Usage

Run the rock paper scissors game:

```sh
python game.py
```

## Testing

Run tests:

```sh
pytest
```
