#gets me the random module so I can use it for the opponent's rock/paper/scissors
import random

#function that will run the rock/paper/scissors game
def rps_game(arg):
    print("You chose: " + arg + ".")
    #random integer between 1-3 will decide computer's position
    num = random.randint(1,3)
    if num == 1:
        opp = "rock"
    elif num == 2:
        opp = "paper"
    elif num == 3:
        opp = "scissors"

    print("The opponent chose: " + opp + ".\n")

    #if statements determine result of game 
    if arg == "rock" and opp == "rock":
        print("You tie.")
    elif arg == "rock" and opp == "paper":
        print("You lose.")
    elif arg == "rock" and opp == "scissors":
        print("You win.")
    elif arg == "paper" and opp == "rock":
        print("You win.")
    elif arg == "paper" and opp == "paper":
        print("You tie.")
    elif arg == "paper" and opp == "scissors":
        print("You lose.")
    elif arg == "scissors" and opp == "rock":
        print("You lose.")
    elif arg == "scissors" and opp == "paper":
        print("You win.")
    elif arg == "scissors" and opp == "scissors":
        print("You tie.")

#game loop
play = True
while play:
    print("Welcome. You are about to play rock/paper/scissors against a randomly generated opponent.\nPlease choose between 'rock', 'paper', or 'scissors'")  
    player = input()
    rps_game(player)
    answer = input("Would you like to play again? (y/n): ")
    if answer == "n":
        play = False  