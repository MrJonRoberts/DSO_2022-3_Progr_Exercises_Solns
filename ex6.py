# basic rock paper scissors
import random
'''
Exercise 6 
Rock Paper Scissors   

Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:

Rock bends scissors
Scissors cut paper
Paper covers rock

#  extension : Rock Paper Scissors Lizard Spock

Scissors cuts paper. 
Paper covers rock. 
Rock crushes lizard. 
Lizard poisons Spock. 
Spock smashes scissors. 
Scissors decapitates lizard. 
Lizard eats paper. 
Paper disproves Spock. 
Spock vaporizes rock. 
Rock crushes scissors.
'''
gameElements = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

outcome = ""
gameOver = False

outcomes = {
    ("Scissors", "Paper") : "CUT",    ('Paper', 'Rock') : "COVERS",
    ('Rock', 'Lizard') : "CRUSHES",    ('Lizard', 'Spock'): "POISONS",
    ('Spock', 'Scissors'): "SMASHES",    ("Scissors", 'Lizard'): "DECAPITATES",
    ('Lizard', 'Paper'): "EATS", ('Paper', 'Spock'): "DISAPROVES",
    ('Spock', 'Rock'): "VAPORIZES", ('Rock', 'Scissors'): "CRUSHES"
}

while not gameOver: # game loop
    # user input.
    userChoice = ""
    while userChoice not in gameElements:
        userChoice = input(f"{gameElements}: ")

    computerChoice = random.choice(gameElements)
    # game here
    if userChoice == computerChoice:
        outcome = f"{userChoice} v {computerChoice}: Draw"
    elif (computerChoice, userChoice) in outcomes:
        outcome = f"Computer Wins:  {computerChoice} {outcomes[computerChoice, userChoice]} {userChoice}"
    elif (userChoice, computerChoice) in outcomes:
        outcome = f"You Win:  {userChoice} {outcomes[userChoice, computerChoice]} {computerChoice}"
    else:
        outcome = "Invalid Choice!"

    print(outcome)
    again = input("Do you want to play again? (y/n) ")
    if again.lower() == "n":
        gameOver = True

print("Thanks for playing")
