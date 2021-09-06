### invader ###
import sys
import pygame
from random import randint
from pygame.locals import QUIT,Rect, KEYDOWN, K_LEFT, K_RIGHT, K_SPACE

pygame.init()
pygame.key.set_repeat(5,5)
SURFACE = pygame.display.set_mode((600,600))
FPSCLOCK = pygame.time.Clock()

class Drawable:
    def __init__(self,rect, offset0,offset1):
        strip = pygame.image.load("image/strip.png")
        self.images = (pygame.Surface((24,24),pygame.SRCALPHA), pygame.Surface((24,24),pygame.SRCALPHA))
        self.rect = rect
        self.count = 0
        self.images[0].blit(strip,(0,0),Rect(offset0,0,24,24))
        self.images[1].blit(strip,(0,0),Rect(offset1,0,24,24))

    def move(self,diff_x,diff_y):
        self.count += 1
        self.rect.move_ip(diff_x,diff_y)
    def draw(self):
        image = self.images[0] if self.count %2 == 0 else self.images[1]
        SURFACE.blit(image,self.rect.topleft)
    
class Ship(Drawable):
    def __init__(self):
        super().__init__(Rect(300,550,24,24),192,192)

class Beam(Drawable):
    def __init__(self):
        super().__init__(Rect(300,0,24,24),0,24)

class Bomb(Drawable):
    def __init__(self):
        super().__init__(Rect(300,-50,24,24),48,72)
        self.time = randint(5,220)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0,0,0))

        pygame.display.update()
        FPSCLOCK.tick(20)
    
if __name__ == "__main__":
    main()