# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:50:17 2024

@author: Steven W
"""

import sys
import os
import time

to_do_dict = {}
key = 0
delete_entry = 0

def clr():
    os.system('cls')
  
def listening():
    print("Enter a command. Type '/help' for more info.")
    
    listened = input(">> ")
    
    if listened == "/help":
        clr()
        help()
        
    elif listened == "/a":
        clr()
        add_to_list()
        
    elif listened == "/v":
        clr()
        print(to_do_dict)
        listening()
        
    elif listened == "/c":
        clr()
        global key
        to_do_dict.clear()
        print("To do has been cleared.")
        print(to_do_dict)
        key = 0
    
    elif listened == "/d":
        clr()
        print(to_do_dict)
        print("Which item would you like to delete?")
        
        delete_entry = input(">>")
        delete_entry = int(delete_entry)
        
        if delete_entry in to_do_dict:
            
            del to_do_dict[delete_entry]
            print("Item deleted.")
            print(to_do_dict)
            time.sleep(1)
            listening()
        else:
            print("Invalid entry, aborting...")
            time.sleep(1)
            listening()
    
    
    elif listened == "/x":
        clr()
        print(to_do_dict)
        print("Which item would you like to mark as completed?")
        complete = input(">>")
        
        complete = int(complete)
        
        if complete in to_do_dict:         
            to_do_dict[complete] += " (x)"
            print("Item marked complete.")
            print(to_do_dict)
            time.sleep(1)
            listening()
        else:
            print("Invalid entry, aborting...")
            time.sleep(1)
            listening()
        
    elif listened == "/e":
        with open('to_do.txt', 'w') as f:
            print(to_do_dict, file=f)
        print("Exported to do list to text file")
        time.sleep(2)
        listening()
        
        
        
        
        
    elif listened == "/q":
        print("Bye bye")
        sys.exit()
        
    else:
        listening()
        
        
def help():
    print("Commands:")
    print("/a - adds to list")
    print("/v - view list")
    print("/d - deletes from list")
    print("/x - to mark entry as done.")
    print("/c - clears the list")
    print("/e - exports to .txt")
    print("/q - exits application")


def add_to_list():
    global key
    
    print("Please enter a task: ")
    to_do = input(">> ")
    key += 1
    
    to_do_dict[key] = to_do
    print(to_do_dict)
    
    
    def add_another():
        print("Add another? y/n:")
        y_or_no = input(">> ")
    
        if y_or_no == "y":
            add_to_list()
        
        elif y_or_no == "n":
            listening()
    
        else:
            add_another()
    add_another()
    
while True:
    listening()