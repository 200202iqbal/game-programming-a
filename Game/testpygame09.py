###testpygame09.py###
import pygame
import sys
from pygame.locals import QUIT,Rect

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    logo = pygame.image.load("image/pythonlogo.jpg")
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        SURFACE.fill((0,0,0))
        SURFACE.blit(logo,(0,0))
        #SURFACE.blit(logo,(250,50))
        SURFACE.blit(logo,(250,50),Rect(50,50,100,100))
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()