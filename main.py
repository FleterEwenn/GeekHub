import subprocess
import sys
import pygame

pygame.init()

window = pygame.display.set_mode((1536, 1024))

run = True

def run_checkpassword():
    subprocess.Popen([sys.executable, "CheckPassword.py"])

bgimage = pygame.image.load("bgimage.png")

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False
    
    window.blit(bgimage, (0, 0))

    pygame.display.flip()