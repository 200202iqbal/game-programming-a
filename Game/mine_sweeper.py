### mine sweeper ###
import pygame
import sys
from pygame.locals import QUIT,MOUSEBUTTONDOWN
from random import randint
from math import floor

pygame.init()
SURFACD = pygame.display.set_mode((1000,750))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
