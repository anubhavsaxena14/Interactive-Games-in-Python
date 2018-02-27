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
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3    
    elif name == "scissors":
        return 4
    else:
        return "Unknown names!"

def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"    
    elif number == 4:
        return "scissors"
    else:
        return "Unknown number!"

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print(" ")
    
    # print out the message for the player's choice
    print("Player chooses " + player_choice)
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
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
    elif diff < 3: # computer wins
        print("Computer wins!")
    else:
        print("Player wins!")
        
if __name__=="__main__":
    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")