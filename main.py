import pygame

pygame.init()

window = pygame.display.set_mode((1000, 600))

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False