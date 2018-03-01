# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:22:35 2018

@author: anubhav
"""

# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3    
    elif name == "scissor":
        return 4
    else:
        return -1

def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"    
    elif number == 4:
        return "scissor"
    else:
        return "Unknown number!"

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print(" ")
    
    # print out the message for the player's choice
    print("Player chooses " + player_choice)
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    if player_number == -1:
        print("Wrong Input")
        return -999
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print("Computer chooses " + comp_choice)
    
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if diff == 0: # a tie!
        print("Player and computer tie!")
        return 0
    elif diff < 3: # computer wins
        print("Computer wins!")
        return -1
    else:
        print("Player wins!")
        return 1        
        
if __name__=="__main__":
    Player = 0
    Computer = 0
    Tie = 0
    Game = 0
    while(True):
        print("Select from Rock \t Paper \t Scissor \t Lizard \t Spock \n")  
        choice = input("Enter your Choice\n")
        winner = rpsls(choice.lower())
    
        Game += 1
        if winner == 0:
            Tie += 1
        elif winner == 1:
            Player += 1
        elif winner == -1:
            Computer += 1
        else:
            break
        play = input("Press E to exit or C to continue ")
        if play == "E":
            break
        else:
            print("Next Game")

        print("Games Played\t" + str(Game))
        
        print("Player Won: " + str(Player) +  "\tComputer Won:  " + str(Computer) + "\tTie: " + str(Tie))

#Result
print("Final Result")
print("Player Won: " + str(Player) +  "\tComputer Won:  " + str(Computer) + "\tTie: " + str(Tie))

print("Thanks for playing")        
        
        