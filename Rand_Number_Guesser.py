# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:15:17 2024

@author: Steven W
"""

import random
import sys
import os

random_number= 0
guesses = 0


def clr():
    os.system('cls')

Running = True

def NumGen():
    global random_number
    random_number=random.randint(1,100)

def GameLoop():
    NumGen()
    
    while Running:
        global guesses
        global random_number
    
        
        user_guess =int(input("Guess a number between 1 and 100:\n>> "))
        guesses += 1

        if user_guess > random_number:
            print("Too high")
            
        elif user_guess< random_number:
            print("Too low")
            
        else:
            clr()
            print(f"The number was {random_number}")
            print(f"You guessed the number in {guesses}")
            PlayAgain()


def PlayAgain():
    global guesses
    print("Play again? y/n")
    play = input(">> ")
    
    if play == 'y':
        clr()
        guesses = 0
        GameLoop()
        
    elif play == 'n':
        sys.exit()
        
    else:
        clr()
        print("Invalid input")
        PlayAgain()
     
    



while True:

    GameLoop()
        