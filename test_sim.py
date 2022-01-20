import pygame
import time
import random 
import sys
import utils

pygame.init()

WIDTH = 500
HEIGHT = 300

GREEN_CAR =  utils.scale_image(pygame.image.load("assets/grey-car.png"), 0.55)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60

class Car:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.ratation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1
    
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    
    def draw(self, run):
        utils.blit_rotate_center(run, self.img, (self.x, self.y), self.angle)
    
    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
    
    


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
