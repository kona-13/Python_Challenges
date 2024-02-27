# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:36:13 2024

@author: Steven
"""

#Okay - this has made some good progress....
#What i want to add is:
    #1.) commands - i.e. attack, bag, etc
    #2.) Basic comp "AI" i.e. give them healing items and shit and they can only use it once if they have health under 30% or some shit
    #3.) "Story", multiple fights, looting, etc, etc.


#Loosely based on https://www.youtube.com/watch?v=cM_ocyOrs_k
import os        
import random
import time
os.system("")

#Class for weapons       
class weapon:
    def __init__(self, name: str, weapon_type: str, damage: float, value: float) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value
        
#List of Weapons
iron_sword = weapon(name = "Iron Sword", weapon_type = "Blade",  damage = 7, value = 10)
short_bow = weapon(name = "Short Bow", weapon_type = "Ranged", damage = 5, value = 4.5)
fists = weapon(name = "Fists", weapon_type = "Blunt", damage = 5, value = 0)      

#Items
class Item:
    def __init__(self, name: str, item_type: str, health_value: float, value: float) -> None:
        self.name = name
        self.item_type = item_type
        self.health_value = health_value
        self.value = value

#List of items        
health_potion = Item(name = "Health Potion", item_type = "Potion", health_value = 20, value = 10)
        
#Class for characters general stuff including player, enemies, boss, etc.
class character:
    def __init__(self, name: str, health: float) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        
        self.weapon = fists
        
    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0) 
        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}.")
        

class player(character):
    def __init__(self, name: str, health: float) -> None:
        super().__init__(name=name, health=health)
        self.default_weapon = self.weapon

        
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped the {self.weapon.name}.")
        
    def item_bagged(self) -> None:
        #self.weapon = self.default_weapon
        #print(f"{self.name} stored the {self.weapon} .")
        self.item = health_potion
        print(f"{self.name} got a {self.item.name}!")
        print(f"{self.name} stored it in the bag.")
        

class Enemy(character):
    def __init__(self, name: str, health: float, weapon, ) -> None:
        super().__init__(name=name, health=health)        
        self.weapon = weapon
        
roll = [0, 1, 2, 3, 4, 5]

commands = ["attack", "Attack", "a", "Bag", "bag", "b", "Flee", "flee", "f"]

world_commands = ["North", "north", "n", "East", "east", "e", "South", "south", "s", "West", "west", "w"]

#Misc functions
def enemy_no_hp():
    item_drop = random.choice(roll)
    
    if item_drop == 1:
        player.item_bagged()
    else:
        print("...")
        
        
def PlayerAttack():
    player.attack(enemy)
    
    
def EnemyAttack():
    enemy.attack(player)
    
def Clear_Screen():
    time.sleep(0.2)
    os.system("cls")
    
def Health_Text():
    print(f"Health of {player.name}: {player.health}.")
    print(f"Health of {enemy.name}: {enemy.health}.")
    
    if enemy.health <= 0:
        print(f"{enemy.name} was slain...")
        enemy_no_hp()
        World_Logic()
        
    elif player.health <= 0:
        print(f"{player.name} has been slain...")
        print("With this, the world is doomed!")
        time.sleep(5)
        exit()

def World_Logic():
    print(f"Which direction will {player.name} go in?")
    print("North, East, South or West?")
    world_direction = input(">> ")
    #Clear_Screen()
    
    if world_direction == "north": #or "north" or "n":
        print(f"{player.name} headed North...")
    elif world_direction == "east": #or "east" or "e":
        print(f"{player.name} headed East...")
    elif world_direction == "south": #or "south" or "s":
        print(f"{player.name} headed South...")
    elif world_direction == "west": #or "west" or "w":            
        print(f"{player.name} headed West...")
            
        battle_initiate = random.choice(roll)
        
        if battle_initiate == 1:
            print(f"{enemy.name} appeared!")
            Battle()
        
        else: 
            print("There is nothing here...")
            World_Logic()
            
    else:
        print("Please enter a valid direction...")
    
    
def Battle():
    
    while True:
        print("Command: Attack | Bag | Flee")
        battle_command = input(">> ")
    
        if battle_command in commands:
        
            if battle_command == "attack": #or "attack" or "a":
                PlayerAttack()
                Health_Text()
                #Clear_Screen()
                
            elif battle_command == "flee":
                print(f"{player.name} ran away...")
                break
                World_Logic()
                
                
        
            else:
                print(f"{player.name} did nothing...")
        
        else:
            print("Enter a valid option...")
        
    
    


print("Enter player name: ")
player_name = input(">> ")        
        
        
        
#Characters
player = player(name = player_name, health = 100)
print(f"{player.name} found a {iron_sword.name} on the floor...")
player.equip(iron_sword)

enemy = Enemy(name = "Enemy", health = 50, weapon = short_bow)



#debug battle
while True:
    
    
    World_Logic()
    
    
    
    #input(">> ")