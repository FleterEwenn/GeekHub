import subprocess
import sys
import pygame
from player import Player

pygame.init()

window = pygame.display.set_mode((1000, 667))

player = Player()
list_module = [pygame.Rect(690, 360, 70, 60), pygame.Rect(720, 200, 75, 75), pygame.Rect(525, 450, 75, 75), pygame.Rect(280, 400, 75, 60)]

run = True

def run_checkpassword():
    subprocess.Popen([sys.executable, "CheckPassword.py"])

bgimage = pygame.image.load("assets/maps/bgimageR.png")

clock = pygame.time.Clock()

while run:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False
    
    player.update(dt)
    
    window.blit(bgimage, (0, 0))

    for i in range(len(list_module)):
        pygame.draw.rect(window, (0, 255, 0), list_module[i], 1)

        if player.rect.left <= list_module[i].right and  player.rect.right >= list_module[i].left \
        and player.rect.bottom >= list_module[i].top and player.rect.top <= list_module[i].bottom :
            if i == 0:
                run_checkpassword()
            player.reset_pos()

    player.draw(window)

    pygame.display.flip()