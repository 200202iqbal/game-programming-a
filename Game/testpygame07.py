### testpygame07.py ###
import pygame
import sys
from pygame import surface
from pygame.locals import QUIT
import random

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
        
        #plist =[(10,10),(210,10),(210,210)]
        plist = []
        for _ in range(10):
            xpos = random.randint(0,400)
            ypos = random.randint(0,300)
            plist.append((xpos,ypos))
        pygame.draw.lines(SURFACE,(255,0,0),True,plist)
        #pygame.draw.lines(SURFACE,(255,0,0),False,plist)

        pygame.display.update()
        FPSCLOCK.tick(1)

if __name__ == "__main__":
    main()