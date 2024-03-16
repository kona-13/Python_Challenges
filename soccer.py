# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:34:48 2024

@author: Steven W
"""

import pygame
import sys
import math
import random


pygame.init()


width, height = 400, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Soccer")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

gravity = 0.7

#rand_x_vel = random.randint(-5, 5)   
#rand_y_vel = random.randint(10, 20)

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity_x = 0
        self.velocity_y = 0 
        self.dragging = False

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        self.velocity_y += gravity

        self.x += self.velocity_x
        self.y += self.velocity_y

        #Bottom collisions;
        if self.y + self.radius >= height:
            self.y = height - self.radius
            self.velocity_y = -self.velocity_y * 0.8 #Loses a lil energy;

        #Sides collisions;
        if self.x + self.radius >= width: #or self.x - self.radius <= 0:
            self.x = width - self.radius
            self.velocity_x = -self.velocity_x
            
        elif self.x - self.radius <= 0:
            self.x = self.radius
            self.velocity_x = -self.velocity_x
            
    #Ball collisions;
    def handle_collision(self, other_ball):
        dx = other_ball.x - self.x
        dy = other_ball.y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < self.radius + other_ball.radius:
            angle = math.atan2(dy, dx)
            overlap = (self.radius + other_ball.radius) - distance

            force_magnitude = overlap * 0.1

            #Maths;
            self.velocity_x -= force_magnitude * math.cos(angle)
            self.velocity_y -= force_magnitude * math.sin(angle)
            other_ball.velocity_x += force_magnitude * math.cos(angle)
            other_ball.velocity_y += force_magnitude * math.sin(angle)

#Main loop;
balls = []
clock = pygame.time.Clock()


points = 0

#Ball spawn;
initial_x = width // 2
initial_y = 50
radius = 75
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
new_ball = Ball(initial_x, initial_y, radius, color)
new_ball.velocity_x = 0
new_ball.velocity_y = 0
balls.append(new_ball)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #Left click;
                for ball in balls:
                    if math.sqrt((event.pos[0] - ball.x)**2 + (event.pos[1] - ball.y)**2) < ball.radius:
                        ball.velocity_x = random.uniform(-5, 5)  #Random x velocity;
                        ball.velocity_y = random.uniform(-35, -20)  #Random y velocity;
                        points += 1
        
        #Spawns a new ball - might repurpose this code later;
        #elif event.type == pygame.MOUSEBUTTONUP:
            #if event.button == 3:
                #radius = random.randint(50, 75)
                #color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                #new_ball = Ball(event.pos[0], event.pos[1], radius, color)
                #balls.append(new_ball)


    screen.fill(WHITE)
    
    #Hitzone;
    mouse_pos = pygame.mouse.get_pos()
    mouse_x, mouse_y = mouse_pos
    square_size = 100  # Adjust as needed
    square_rect = pygame.Rect(mouse_x - square_size // 2, mouse_y - square_size // 2, square_size, square_size)
    pygame.draw.rect(screen, RED, square_rect, 2)

    for ball in balls:
        ball.update()
        ball.draw()
        if ball.y + ball.radius >= height:  #Check if the ball touches the bottom of the screen - then sets points to 0;
            points = 0

    #Ball on ball collisions;
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            balls[i].handle_collision(balls[j])

    #Points;
    points_text = pygame.font.SysFont(None, 24).render(f"Points: {points}", True, BLACK)
    screen.blit(points_text, (width - 100, 10))

    #FPS;
    fps = int(clock.get_fps())
    fps_text = pygame.font.SysFont(None, 24).render(f"FPS: {fps}", True, BLACK)
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()


    clock.tick(60)

pygame.quit()
sys.exit()
