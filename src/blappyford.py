import pygame
import math
import random

# Constants

WIDTH = 1080
HEIGHT = 720
SCREEN_COLOR = (0,0,0)
MAX_WALL_SIZE = HEIGHT-100

class Wall():
    def __init__(self, height, altitude):
        self.height = height
        self.speed = 100
        self.pos = ([WIDTH,altitude])
        self._rect = pygame.Rect(self.pos[0],self.pos[1],WIDTH/20,self.height)

    def update (self,dt):
        self.pos[0] -= self.speed*dt   
        self._rect = pygame.Rect(self.pos[0],self.pos[1],WIDTH/30,self.height)

    def is_offscreen(self):
        wall_is_offscreen = (self.pos[0] <= 0)
        return wall_is_offscreen

    def draw(self,surface):
        pygame.draw.rect(surface,(255,0,0),self._rect)

class WallPair():
    def __init__(self):
        self.topheight = random.randrange(100,MAX_WALL_SIZE)
        self.botheight = HEIGHT
        while (HEIGHT-self.botheight < self.topheight + 60):
            self.botheight = random.randrange(100,MAX_WALL_SIZE)
        self.walls = []
        self._makewallpair()

    def _makewallpair(self):
        self.walls.append(Wall(self.topheight,0))
        self.walls.append(Wall(self.botheight,HEIGHT-self.botheight))
    
    def update(self,dt):
        for wall in self.walls:
            wall.update(dt)

    def _is_offscreen(self):
        return self.walls[0].is_offscreen()
    
    def draw(self,surface):
        for wall in self.walls:
            wall.draw(surface)

def main():
    pygame.init()
    pygame.display.set_caption("Adventures of Blappyford")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,24)
    dt = 0
    walls = WallPair()

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Game Logic
        walls.update(dt)
        # Render & Display
        screen.fill(SCREEN_COLOR)
        walls.draw(screen)
        pygame.display.flip()
        dt = clock.tick(30)/1000.0

    pygame.quit()


if __name__ == "__main__":
    main()