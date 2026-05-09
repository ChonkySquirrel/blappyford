import pygame
import math
import random

# Constants

WIDTH = 1080
HEIGHT = 720
SCREEN_COLOR = (0,0,0)
MAX_WALL_SIZE = HEIGHT-100
MAX_WALL_SPEED = 200
MIN_WALL_GAP = 70
MIN_SPAWN_TIME = 1.6

class Particle():
    def __init__(self, pos=(0,0), size=15, life=500):
        self.pos = pos
        self.size = size
        self.biggest_size = size
        self.age = 0
        self.life = life
        self.color = pygame.Color(0,100,0,255)
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size,self.size)
        self.dead = False

    def update(self,dt):
        self.age += dt
        self.color = pygame.Color(0,100,0,255 * (1 - self.age/self.life))
        self.rect.scale_by_ip(1 - (self.age/self.life))
        self.rect.center = (self.pos[0]+self.size/(1 - self.age/self.life)/2,self.pos[1]+self.size/(1 - self.age/self.life)/2)
        if self.age > self.life:
            self.dead = True
    
    def draw(self, surface):
        if self.dead:
            return
        pygame.draw.rect(surface, self.color, self.rect, border_radius = 2)


class Player():
    def __init__(self):
        x = WIDTH//30
        y = HEIGHT//2
        self.rect = pygame.Rect(x,y, 20,20)
        self.spdx = 180
        self.vely = 0
        self.jump_force = 8
        self.gravity = 15
        self.jumpsound = pygame.mixer.Sound("jumpsound.wav")
        self.trail = []
    
    def _is_jumping (self, events):
        for event in events:
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE:
                    self.jumpsound.play()
                    return True
        return False

    def update(self, keys, tap, dt):
        dx = 0.0
        self.vely -= self.gravity*dt
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= self.spdx * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += self.spdx * dt
        if self._is_jumping(tap):
                self.vely = self.jump_force
        self.rect.x = int(round(self.rect.x + dx))
        self.rect.y = int(round(self.rect.y - self.vely))
        self.rect.clamp_ip(pygame.Rect(0,0, WIDTH, HEIGHT))
        self.update_trail(dt)
    
    def update_trail(self,dt):
        new_particle = Particle((self.rect.x, self.rect.y), self.rect.width, 500)
        self.trail.insert(0,new_particle)
        for idx, particle in enumerate(self.trail):
            particle.update(dt)
            if particle.dead:
                del self.trail[idx]

    def draw(self, surface):
        for particle in self.trail:
            particle.draw(surface)
        pygame.draw.rect(surface, (0,200,0), self.rect, border_radius = 2)

class Wall():
    def __init__(self, height, altitude, points):
        self.height = height
        self.speed = 100 + points*2
        self._speed_snap()
        self.pos = ([WIDTH,altitude])
        self.rect = pygame.Rect(self.pos[0],self.pos[1],WIDTH/20,self.height)
    
    def _speed_snap(self):
        if self.speed > MAX_WALL_SPEED:
            self.speed = MAX_WALL_SPEED

    def update (self,dt):
        self.pos[0] -= self.speed*dt   
        self.rect = pygame.Rect(self.pos[0],self.pos[1],WIDTH/30,self.height)

    def is_offscreen(self):
        wall_is_offscreen = (self.pos[0] <= 0-WIDTH/20)
        return wall_is_offscreen

    def draw(self,surface):
        pygame.draw.rect(surface,(200,0,0),self.rect)

class WallPair():
    def __init__(self,points):
        self.diff = points
        self.gap = 200 - points*2
        self._gap_snap()
        self.topheight = random.randrange(100,MAX_WALL_SIZE)
        self.botheight = HEIGHT - self.topheight - self.gap
        self.walls = []
        self.rects = []
        self.cleared = False
        self.pos = WIDTH
        self._make_wall_pair()
    
    def _gap_snap(self):
        if self.gap < MIN_WALL_GAP:
            self.gap = MIN_WALL_GAP

    def _make_wall_pair(self):
        self.walls.append(Wall(self.topheight,0,self.diff))
        self.rects.append(self.walls[0].rect)
        self.walls.append(Wall(self.botheight,HEIGHT-self.botheight,self.diff))
        self.rects.append(self.walls[1].rect)
    
    def update_walls(self,dt):
        idx = 0
        for wall in self.walls:
            wall.update(dt)
            self.rects[idx] = wall.rect
            self.pos = wall.pos[0]
            idx += 1

    def can_give_points(self):
        if self.cleared == False:
            return True
        return False

    def clear(self):
        print("Obstacle Cleared!")
        self.cleared = True

    def is_offscreen(self):
        return self.walls[0].is_offscreen()
    
    def draw(self,surface):
        for wall in self.walls:
            wall.draw(surface)

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Adventures of Blappyford")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,24)
    font_large = pygame.font.Font(None,36)
    font_huge = pygame.font.Font(None,48)
    dt = 0.0
    pointsound = pygame.mixer.Sound("pointget.wav")
    deathsound = pygame.mixer.Sound("deathsound.wav")
    walls = []
    spawn_timer = 4
    points = 0
    player = Player()
    game_over = False
    spawn_interval = 4
    running = True
    while running:
        # Event Loop
        keys = pygame.key.get_pressed()
        inputs = pygame.event.get()
        for event in inputs:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE:
                    if game_over:
                        player = Player()
                        walls = []
                        points = 0
                        spawn_timer = 4
                        game_over = False
        # Game Logic
        if not game_over:
            player.update(keys,inputs,dt)
            if spawn_interval >= MIN_SPAWN_TIME:
                spawn_interval = 4 - (0.2*(points//5))
            spawn_timer += dt
            if spawn_timer >= (spawn_interval+(random.randrange(-2,2)/10)):
                spawn_timer = 0.0
                walls.append(WallPair(points))
            
            for idx, wall in enumerate(walls):
                if wall.is_offscreen():
                    del walls[idx]
                    walls[idx].update_walls(dt)
                if player.rect.x >= wall.pos and wall.can_give_points():
                    wall.clear()
                    points += 1
                    pointsound.play()
                    print (f"Point earned! Now at {points} points!")
                wall.update_walls(dt)
            for wall in walls:
                for rect in wall.rects:
                    if player.rect.colliderect(rect):
                        game_over = True
                        deathsound.play()
                        print("OUCH!")
                        break
         
        # Render & Display
        screen.fill(SCREEN_COLOR)
        player.draw(screen)
        for wall in walls:
            wall.draw(screen)
        if game_over:
            overlay_back = pygame.Rect(WIDTH/5,HEIGHT/5*2,WIDTH*0.6,HEIGHT*0.2)
            pygame.draw.rect(screen,(0,0,0),overlay_back,border_radius = 6)
            game_overlay = font_large.render(f"GAME OVER - FINAL SCORE: {points} - JUMP TO RESTART",True,(255,255,255))
            screen.blit(game_overlay,game_overlay.get_rect(center=(WIDTH//2,HEIGHT//2)))
        if not game_over:
            score = font_huge.render(f"SCORE: {points}",True,(255,255,255))
            score_back_width = 160 + 20*(len(str(points)))
            score_back = pygame.Rect((WIDTH/5*4)-10,4,score_back_width,68)
            controls = font.render("Arrows / AD to move - Jump with Space / W / Up",True,(120,120,120))
            screen.blit(controls, (12, 12))
            pygame.draw.rect(screen,(45,45,45),score_back,border_radius=3)
            screen.blit(score, (WIDTH/5*4,24))
        pygame.display.flip()
        dt = clock.tick(30)/1000.0

    pygame.quit()


if __name__ == "__main__":
    main()