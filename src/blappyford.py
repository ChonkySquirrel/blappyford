import pygame
import math
import random

# Constants

WIDTH = 1080
HEIGHT = 720
SCREEN_COLOR = (0,0,0)

class BottomWall():
    def __init__(self):
        self.height = 200
        self.speed = 100
        self.pos = ([WIDTH,HEIGHT-self.height])
        self._rect = pygame.Rect(self.pos[0],self.pos[1],WIDTH/20,self.height)

    def update (self,dt):
        self.pos[0] -= self.speed*dt   
        self._rect = pygame.Rect(self.pos[0],self.pos[1],WIDTH/30,self.height)

    def _is_offscreen(self):
        wall_is_offscreen = (self.pos[0] <= 0)
        return wall_is_offscreen

    def draw(self,surface):
        pygame.draw.rect(surface,(255,0,0),self._rect)


def main():
    pygame.init()
    pygame.display.set_caption("Adventures of Blappyford")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,24)
    dt = 0
    wall = BottomWall()

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Game Logic
        wall.update(dt)
        # Render & Display
        screen.fill(SCREEN_COLOR)
        wall.draw(screen)
        pygame.display.flip()
        dt = clock.tick(30)/1000.0

    pygame.quit()


if __name__ == "__main__":
    main()