###testpygame11.py###
import pygame
import sys
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    logo = pygame.image.load("image/pythonlogo.jpg")
    theta = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0,0,0))
        theta+=1
        new_logo =pygame.transform.rotate(logo,theta)
        SURFACE.blit(new_logo,(100,30))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()