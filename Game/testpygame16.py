## testpygame16.py ##
import pygame 
import sys
from pygame.locals import QUIT
from math import sin, cos, radians

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0,0,0))
        plist0,plist1 = [],[]
        for theta in range(0,720,144):
            rad = radians(theta)
            plist0.append((cos(rad)*100 + 100,sin(rad)*100+150))
            plist1.append((cos(rad)*100 + 100,sin(rad)*100+150))
        pygame.draw.lines(SURFACE,(255,255,255),True,plist0,5)
        pygame.draw.aalines(SURFACE,(255,255,255),True,plist1)
        pygame.display.update()
        FPSCLOCK.tick(3)


if __name__ == "__main__":
    main()