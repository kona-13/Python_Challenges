# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:36:13 2024

@author: Steven
"""
#Loosely based on https://www.youtube.com/watch?v=cM_ocyOrs_k
import os        
os.system("")

#Class for weapons       
class weapon:
    def __init__(self, name: str, weapon_type: str, damage: float, value: float) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value
        
#Weapons
iron_sword = weapon(name = "Iron Sword", weapon_type = "Blade",  damage = 7, value = 10)
short_bow = weapon(name = "Short Bow", weapon_type = "Ranged", damage = 5, value = 4.5)
fists = weapon(name = "Fists", weapon_type = "Blunt", damage = 5, value = 0)        
        
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
        
    def bagged(self) -> None:
        self.weapon = self.default_weapon
        print(f"{self.name} stored the {self.weapon} .")

class Enemy(character):
    def __init__(self, name: str, health: float, weapon, ) -> None:
        super().__init__(name=name, health=health)        
        self.weapon = weapon
        
print("Enter player name: ")
player_name = input(">> ")        
        
        
        
#Characters
player = player(name = player_name, health = 100)
player.equip(iron_sword)
enemy = Enemy(name = "Enemy", health = 50, weapon = short_bow)

#Items




while True:
    
    os.system("cls")
    player.attack(enemy)
    enemy.attack(player)
    

    print(f"Health of {player.name}: {player.health}.")
    print(f"Health of {enemy.name}: {enemy.health}.")
    
    input(">> ")