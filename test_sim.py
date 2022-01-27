import pygame
import time
import random
import math 
import sys
import utils

pygame.init()

# WIDTH = 500
# HEIGHT = 300

GRASS = utils.scale_image(pygame.image.load("assets/grass-py.jpg"), 2.5)

TRACK = utils.scale_image(pygame.image.load("assets/track_py.png"), 0.9)

TRACK_BORDER = utils.scale_image(pygame.image.load("assets/track-border.png"), 0.9)

GRAY_CAR =  utils.scale_image(pygame.image.load("assets/grey-car.png"), 0.55)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pygame Testing!")

FPS = 60

class Car:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
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

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

class PlayerCar(Car):
    IMG = GRAY_CAR
    START_POS = (180, 200)

def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    pygame.display.update()


run = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0))]
player_car = PlayerCar(4, 4)

while run:

    clock.tick(FPS)

    draw(SCREEN, images, player_car)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()

    if not moved:
        player_car.reduce_speed()

pygame.quit()
