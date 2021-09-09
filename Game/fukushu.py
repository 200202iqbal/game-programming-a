from invader import FPSCLOCK
import pygame
import sys
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

        pygame.draw.rect(SURFACE,(255,0,0),(10,20,100,50))
        pygame.draw.circle(SURFACE,(0,255,0),(100,150),40)
        pygame.draw.rect(SURFACE,(255,0,0),(200,20,100,100))
        pygame.draw.ellipse(SURFACE,(0,0,255),(200,20,100,100))
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()
