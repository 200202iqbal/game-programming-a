### fukushu3.py ###
from fukushu2 import FPSCLOCK, SURFACE
import pygame
import sys
from pygame.locals import QUIT
import random

pygame.init()
SURFACE  =pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    x = random.randint(0,300)
    y = random.randint(0,200)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        SURFACE.fill((255,255,255))
        pygame.draw.rect(SURFACE,(255,0,0),(x,y,100,100))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()