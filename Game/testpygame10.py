### testpygame10.py ###
import pygame
import sys
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT,K_RIGHT,K_UP,K_DOWN

pygame.init()
pygame.key.set_repeat(5,5)
SURFACE = pygame.display.set_mode((300,200))
FPSCLOCK = pygame.time.Clock()

def main():
    strip = pygame.image.load("image/strip.png")
    images = []
    for index in range(9):
        image = pygame.Surface((24,24))
        image.blit(strip,(0,0),Rect(index*24,0,24,24))
        images.append(image)

    counter = 0
    pos_x = 100
    pos_y = 150
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pos_x-=1
                elif event.key == K_RIGHT:
                    pos_x+=1
                elif event.key == K_UP:
                    pos_y-=1
                elif event.key == K_DOWN:
                    pos_y+=1
        SURFACE.fill((0,0,0))
        SURFACE.blit(images[counter%2+0],(50,50))
        SURFACE.blit(images[counter%2+2],(100,50))
        SURFACE.blit(images[counter%2+4],(150,50))
        SURFACE.blit(images[counter%2+6],(200,50))
        counter+=1
        SURFACE.blit(images[8],(pos_x,pos_y))
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()