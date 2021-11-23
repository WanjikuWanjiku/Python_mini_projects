#rock, paper, scissors

import random

def rock_paper_scissors():
    player_1 = random.choice(("rock","paper","scissors"))
    player_2 = input("Enter either: r for rock, p for paper or s for scissors: ")
   
    if player_1 == "rock" and player_2 == "r" or player_1 == "paper" and player_2 == "p" or player_1 =="scissors" and player_2 == "s":
        print(f"Computer : {player_1} \nYou : {player_2}")
        print("It's a draw!\n")
        
    elif player_1 == "paper" and player_2 == "r" or player_1 == "scissors" and player_2 == "p" or player_1 =="rock" and player_2 == "s":
        print(f"Computer : {player_1} \nYou : {player_2}")
        print("Computer wins!\n")
        
    elif player_1 == "paper" and player_2 == "s" or player_1 == "paper" and player_2 == "r" or player_1 =="scissors" and player_2 == "r":
       print(f"Computer : {player_1} \nYou : {player_2}")
       print("You win!\n")
    else:
        print("Wrong Entry\n")
    

count = 0
while count < 5:
    rock_paper_scissors()
    count += 1


print("Game Over!")
