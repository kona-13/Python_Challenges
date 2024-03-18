# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:42:12 2024

@author: Steven W
"""


import pygame
import sys
import math
import random
import time

pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Not Flappy Bird")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

gravity = 0.7

hi_score = 0

class Bird:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity_y = 0

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        self.velocity_y += gravity
        self.y += self.velocity_y

        if self.y + self.radius >= height:
            self.y = height - self.radius
            self.velocity_y = 0

class Pipe:
    def __init__(self, x, gap_y, gap_height, width):
        self.x = x
        self.gap_y = gap_y
        self.gap_height = gap_height
        self.width = width
        self.color = GREEN
        self.stopped = False
        self.passed = False

    def draw(self):
        top_pipe_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        bottom_pipe_rect = pygame.Rect(self.x, self.gap_y + self.gap_height, self.width, height - (self.gap_y + self.gap_height))
        pygame.draw.rect(screen, self.color, top_pipe_rect)
        pygame.draw.rect(screen, self.color, bottom_pipe_rect)

    def update(self, velocity):
        if not self.stopped:
            self.x -= velocity

def check_collision(bird, pipes):
    for pipe in pipes:
        if (bird.x + bird.radius > pipe.x and bird.x - bird.radius < pipe.x + pipe.width and
                (bird.y - bird.radius < pipe.gap_y or bird.y + bird.radius > pipe.gap_y + pipe.gap_height)):
            bird.velocity_y *= -0.5  #Reduces the vertical velocity and change direction;
            bird.x -= 10  #Moves the bird slightly backward;
            return True
    return False

def game_loop():
    global points, pipes, pipe_width, pipe_speed, hi_score

    birds = [Bird(width // 4, height // 2, 20, YELLOW)]
    pipes = []
    points = 0
    pipe_width = 50
    pipe_speed = 3
    spawn_pipe_event = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_pipe_event, 1500)

    clock = pygame.time.Clock()
    running = True
    

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if not any(pipe.stopped for pipe in pipes):
                        birds[0].velocity_y = -10     

            elif event.type == spawn_pipe_event:
                if not any(pipe.stopped for pipe in pipes):
                    #gap_y = random.randint(100, height - 300) #This line sometimes causes the gap to be non existent;
                    gap_y = random.randint(100 + 3 * birds[0].radius, height - 300) #Replaced with this but it is a big gap...;
                    pipes.append(Pipe(width, gap_y, 200, pipe_width))

        screen.fill(WHITE)
        
        for bird in birds:
            bird.update()
            bird.draw()

        for pipe in pipes:
            pipe.draw()
            pipe.update(pipe_speed)
            
            if not pipe.stopped and not pipe.passed and birds[0].x > pipe.x + pipe.width:
                pipe.passed = True
                points += 1

        pipes = [pipe for pipe in pipes if pipe.x + pipe.width > 0]
        
        #FPS;
        fps = int(clock.get_fps())
        fps_text = pygame.font.SysFont(None, 24).render(f"FPS: {fps}", True, BLACK)
        screen.blit(fps_text, (10, 10))

        
        #Collision with pipe or floor causes pause and game over;
        if check_collision(birds[0], pipes):
            print("Game Over")
            for pipe in pipes:
                pipe.stopped = True
            birds[0].velocity_y = 0
            
        if birds[0].y + birds[0].radius >= height:
            time.sleep(1.5) #Pause before calling the game loop function again - this is probably a shit way to do it but it works;
            game_loop()

        #Points & Hi-Score stuff;
        points_text = pygame.font.SysFont(None, 24).render(f"Points: {points}", True, BLACK)
        screen.blit(points_text, (width - 100, 10))
                
        if points > hi_score:
            hi_score = points
        
        hi_score_text = pygame.font.SysFont(None, 24).render(f"Hi-Score: {hi_score}", True, BLACK)
        screen.blit(hi_score_text, (width - 200, 10))

        pygame.display.flip()
        clock.tick(60)
        


game_loop()

pygame.quit()
sys.exit()
