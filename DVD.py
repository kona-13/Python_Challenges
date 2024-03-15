# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:34:48 2024

@author: Steven W
"""

import pygame
import sys
import os
import random

pygame.init()

#Get the current dir;
script_dir = os.path.dirname(__file__)

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DVD")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

rand_x = random.randint(100, 500)
rand_y = random.randint(100, 300)

#Load DVD image;
dvd_image = pygame.image.load(os.path.join(script_dir, "DVD.png")).convert_alpha()

class DVD(pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed):
        super().__init__()
        self.original_image = image.copy()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.dx = speed  #Gives initial movement;
        self.dy = speed  #Same as above;
        self.color = WHITE  #Initial color;

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        #Check for collision with screen edges + reverses pos;
        if self.rect.x <= 0 or self.rect.x >= width - self.rect.width:
            self.dx *= -1
            self.change_color()
        if self.rect.y <= 0 or self.rect.y >= height - self.rect.height:
            self.dy *= -1
            self.change_color()

    #Random color gen + reloading image - because I coudln't think of an easier way to do it and it just works haha;
    def change_color(self):
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.image = self.original_image.copy()
        self.image.fill(self.color, special_flags=pygame.BLEND_RGB_MULT)

clock = pygame.time.Clock()
running = True
show_fps = False

#DVD Object;
dvd = DVD(rand_x, rand_y, dvd_image, 5)
all_sprites = pygame.sprite.Group(dvd)

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                new_dvd = DVD(random.randint(0, width - dvd_image.get_width()),
                      random.randint(0, height - dvd_image.get_height()),
                      dvd_image, 5)
                all_sprites.add(new_dvd)
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                show_fps = not show_fps
            

    
    
    
    all_sprites.update()
    all_sprites.draw(screen)
    
    #Commented out FPS - might make this a button press to turn on;
    if show_fps:
        fps = int(clock.get_fps())
        fps_text = pygame.font.SysFont(None, 24).render(f"FPS: {fps}", True, WHITE)
        screen.blit(fps_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
