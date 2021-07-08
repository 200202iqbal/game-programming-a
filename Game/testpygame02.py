### testpygame02.py ###
import pygame
import sys
from pygame.locals import QUIT,Rect

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()
        SURFACE.fill(255,255,255)

        pygame.display.update()
        FPSCLOCK.tick(1)

if __name__ == "__main__":
    main()