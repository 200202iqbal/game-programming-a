### testpygame06.py ###
import pygame
import sys
from pygame import surface
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        SURFACE.fill((255,255,255))
        
        for xpos in range(0,400,25): #dari 0 sampai 400 dengan step 25
            pygame.draw.line(SURFACE,(0,0,255),(xpos,0),(xpos,300))

        for ypos in range(0,300,25):
            pygame.draw.line(SURFACE,(0,0,255),(0,ypos),(400,ypos))
        pygame.display.update()
        FPSCLOCK.tick(1)

if __name__ == "__main__":
    main()