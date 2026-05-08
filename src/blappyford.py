import pygame
import math
import random

# Constants

WIDTH = 1080
HEIGHT = 720
SCREEN_COLOR = (0,0,0)
MAX_WALL_SIZE = HEIGHT-100

class Player():
    def __init__(self):
        x = WIDTH//30
        y = HEIGHT-20//2
        self.rect = pygame.Rect(x,y, 20,20)
        self.spdx = 50
        self.vely = 0
        self.jump_force = 40
        self.gravity = 5
    
    def update(self, keys, dt):
        dx = 0.0
        self.vely -= 10*dt
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= self.spdx * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += self.spdx * dt
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vely = self.jump_force
        self.rect.x = int(round(self.rect.x + dx))
        self.rect.y = int(round(self.rect.y + self.vely))
        self.rect.clamp_ip(pygame.Rect(0,0 WIDTH, HEIGHT))

    def draw(self, surface):
        pygame.draw.rect(surface, (0,255,0), self.rect, border_radius = 2)
        


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
        self.botheight = HEIGHT - self.topheight - 200
        self.walls = []
        self._make_wall_pair()

    def _make_wall_pair(self):
        self.walls.append(Wall(self.topheight,0))
        self.walls.append(Wall(self.botheight,HEIGHT-self.botheight))
    
    def update_walls(self,dt):
        for wall in self.walls:
            wall.update(dt)

    def is_offscreen(self):
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
    dt = 0.0
    walls = []
    spawn_timer = 4
    player = Player()

    running = True
    while running:
        # Event Loop
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Game Logic

        player.update(keys,dt)

        spawn_timer += dt
        if spawn_timer >= 4:
            spawn_timer = 0.0
            walls.append(WallPair())
        
        for idx, wall in enumerate(walls):  
            if wall.is_offscreen():
                del walls[idx]
                walls[idx].update_walls(dt)
            wall.update_walls(dt)
         
        # Render & Display
        screen.fill(SCREEN_COLOR)
        for wall in walls:
            wall.draw(screen)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(30)/1000.0

    pygame.quit()


if __name__ == "__main__":
    main()