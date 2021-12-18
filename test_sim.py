import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    screen.fill((0, 0, 0))

    pygame.draw.cricle(screen, (0,0,255),(250, 250), 75)

    pygame.display.flip()

pygame.quit()