###block.py###

import pygame
import sys
import math
import random
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,Rect

pygame.init()
pygame.key.set_repeat(5,5)
SURFACE = pygame.display.set_mode((600,800))
FPSCLOCK = pygame.time.Clock()

class Block:
    def __init__(self,col,rect,speed=0):
        self.col = col
        self.rect =rect
        self.speed = speed
        self.dir = random.randint(-45,45) + 270
    
    def move(self):
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery += math.sin(math.radians(self.dir)) * self.speed
    def draw(self):
        if self.speed == 0:
            pygame.draw.rect(SURFACE,67self.col,self.rect)

BLOCKS = []
PADDLE = Block((242,242,0), Rect(300,700,100,30))
BALL = Block((242,242,0),Rect(300,400,20,20),10)

def tick():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def main():
    fps = 30
    myfont = pygame.font.SysFont(None,80)
    mess_clear = myfont.render("Cleared!",True,(255,255,0))
    mess_over = myfont.render("Game Over !", True, (255,255,0))
    colors = [(255,0,0),(255,165,0),(242,242,0),(0,128,0),(128,0,128),(0,0,250)]
    for ypos,color in enumerate(colors,start = 0):
        for xpos in range(0,5):
            BLOCKS.append(Block(color,Rect(xpos * 100 + 60,)))

    while True:
        tick()
        SURFACE.fill((0,0,0))

        pygame.display.update()
        FPSCLOCK.tick(fps)

if __name__ == "__main__":
    main()