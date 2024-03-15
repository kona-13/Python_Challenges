# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:34:48 2024

@author: Steven W
"""

import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Physics Test")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define constants
gravity = 0.5

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity_x = 0  # Initial x-axis velocity
        self.velocity_y = 0  # Initial y-axis velocity
        self.dragging = False

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        # Apply gravity
        self.velocity_y += gravity

        # Update position
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Check for collisions with the bottom of the screen
        if self.y + self.radius >= height:
            self.y = height - self.radius
            self.velocity_y = -self.velocity_y * 0.8  # Bounce with some loss of energy

        # Check for collisions with the sides of the screen
        if self.x + self.radius >= width: #or self.x - self.radius <= 0:
            self.x = width - self.radius
            self.velocity_x = -self.velocity_x
            
        elif self.x - self.radius <= 0:
            self.x = self.radius
            self.velocity_x = -self.velocity_x
            

    def handle_collision(self, other_ball):
        dx = other_ball.x - self.x
        dy = other_ball.y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < self.radius + other_ball.radius:
            angle = math.atan2(dy, dx)
            overlap = (self.radius + other_ball.radius) - distance

            # Calculate the force magnitude based on the overlap
            force_magnitude = overlap * 0.1  # Adjust this factor to control the strength of the repelling force

            # Apply the force to both balls
            self.velocity_x -= force_magnitude * math.cos(angle)
            self.velocity_y -= force_magnitude * math.sin(angle)
            other_ball.velocity_x += force_magnitude * math.cos(angle)
            other_ball.velocity_y += force_magnitude * math.sin(angle)

# Main game loop
balls = []
clock = pygame.time.Clock()  # Create a clock object
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for ball in balls:
                    if math.sqrt((event.pos[0] - ball.x)**2 + (event.pos[1] - ball.y)**2) < ball.radius:
                        ball.dragging = True
            elif event.button == 3:
                # Spawn a new ball with random color and size between red and max size
                radius = random.randint(20, 75)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                new_ball = Ball(event.pos[0], event.pos[1], radius, color)
                balls.append(new_ball)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for ball in balls:
                    if ball.dragging:
                        # Calculate velocity based on mouse movement
                        ball.velocity_x = (event.pos[0] - ball.x) / 3  # Adjust divisor to control velocity
                        ball.velocity_y = (event.pos[1] - ball.y) / 3  # Adjust divisor to control velocity
                        ball.dragging = False

    # Clear the screen
    screen.fill(WHITE)
    
    fps = int(clock.get_fps())
    fps_text = pygame.font.SysFont(None, 24).render(f"FPS: {fps}", True, BLACK)
    screen.blit(fps_text, (10, 10))

    # Update and draw balls
    for ball in balls:
        if ball.dragging:
            ball.x, ball.y = pygame.mouse.get_pos()
            ball.velocity_x = 0
            ball.velocity_y = 0
        ball.update()
        ball.draw()

    # Check for collisions between balls
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            balls[i].handle_collision(balls[j])

    # Update the display
    pygame.display.flip()

    # Draw FPS
    fps = int(clock.get_fps())
    fps_text = pygame.font.SysFont(None, 24).render(f"FPS: {fps}", True, BLACK)
    screen.blit(fps_text, (10, 10))

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
