import pygame
import time
import random 
import sys

pygame.init()

WIDTH = 500
HEIGHT = 300

GREEN_CAR = pygame.image.load("assets/green-car.png")

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            run = False

    
    SCREEN.fill((0, 0, 0))

    pygame.draw.circle(SCREEN, (0,255,0),(250, 250), 75)

    pygame.display.flip()

pygame.quit()

#Chequear materias banner