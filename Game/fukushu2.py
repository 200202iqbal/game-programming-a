###fukushu2.py###
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
        for y in range(2):
            for x in range(4):
                pygame.draw.rect(SURFACE,(y * 100 + x,0,0),(x * 100+10 ,y * 150 + 50,50,100))
        
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()