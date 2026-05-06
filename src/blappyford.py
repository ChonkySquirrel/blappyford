import pygame
import math
import random

def main():
    pygame.init()
    pygame.display.set_caption("Adventures of Blappyford")
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,24)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()