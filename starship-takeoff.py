# my attempt at converting starship take off into python - originally written in basic - idea taken from https://usborne.com/gb/books/computer-and-coding-books

import random
import os
import sys

# variables;
g = 0
w = 0
r = 0
c = 10 # gusesses;

def clr():
    os.system('cls')

def roll():
    global g, w, r
    g = random.randint(1,20)
    w = random.randint(1,40)
    r = w * g
    
def again():
    global c
    print("Play again? y/n")
    play = input(">> ")
    
    if play == 'y':
        clr()
        c = 10
        logic()
        
    elif play == 'n':
        sys.exit()
        
    else:
        clr()
        print("Invalid input")
        again()

def logic():
    global c
    clr()
    roll()
    print("You are a starship captain. You have crashed your ship on a strange planet and must take off again quickly in the alien ship you have captured. The ship's computer tells you the gravity on the planet. You must guess the force required for a successful take off.")
    print(f"gravity = {g}")
    
    
    while c > 0:
        f = int(input("Enter a force (integer):\n>>"))
        c -= 1
    
        if f > r:
            print("Too high")
            print(f"Attempts left: {c}")
     
        elif f < r:
            print("Too low")
            print(f"Attempts left: {c}")
    
        elif f == r:
            print("You win!")
            again()
        
        elif c <= 0:
            break
        
    print("You Failed...")
    print("The aliens got you.")
    again()
        
    
logic()