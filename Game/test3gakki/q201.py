### 学生番号 : 200202
### 名前 : ムハンマドイクバルタワカル

import pygame
import sys
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((600,600))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        SURFACE.fill((255,255,255))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()