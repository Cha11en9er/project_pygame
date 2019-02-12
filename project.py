import os
import pygame
from random import randint

pygame.init()
size = (400, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
shipposx = 0

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
        image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

class My_ship(pygame.sprite.Sprite):
    wall = load_image("space_ship.png")
    image = pygame.transform.scale(wall, (50, 50))
    possition = 175

    def __init__(self, group):
        super().__init__(group)
        self.image = My_ship.image
        self.rect = self.image.get_rect()
        self.rect.x = 175
        self.rect.y = 400

    def get_event(self, event):
        #print('event')
        if self.rect.collidepoint(event.pos):
            self.image = self.image

    def update(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.rect.x -= 10
                shipposx = self.rect.x
                My_ship.possition = shipposx
            elif event.key == pygame.K_d:
                self.rect.x += 10
                shipposx = self.rect.x
                My_ship.possition = shipposx


class Enemy_ship(pygame.sprite.Sprite):  
    star = load_image("car2.png")
    image = pygame.transform.scale(star, (50, 50))

    def __init__(self, group):
        super().__init__(group)
        self.image = Enemy_ship.image
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 450)
        self.rect.y = -50
    
    def update(self):
        v = 100
        fps = 100
        self.rect.y += v / fps
        if int(self.rect.y) == 400:
            self.kill() 
        clock.tick(fps)

class Rocket(pygame.sprite.Sprite):
    Lazer = load_image("rocket.png")
    image = pygame.transform.scale(Lazer, (10, 25))

    def __init__(self, group):
        super().__init__(group)
        self.image = Rocket.image
        self.rect = self.image.get_rect()

        self.rect.x = shipposx + 22.5
        
        self.rect.x = My_ship.possition + 22.5
        self.rect.y = 415
    
    def update(self):
        #print(shipposx)
        v = 300
        fps = 100
        self.rect.y -= v / fps
        clock.tick(fps)
        

class Wall(pygame.sprite.Sprite):
    wall = load_image("space.png")
    image = pygame.transform.scale(wall, (400, 500))

    def __init__(self, group):
        super().__init__(group)
        self.image = Wall.image
        self.rect = self.image.get_rect()  

class Star(pygame.sprite.Sprite):  
    star = load_image("star.png")
    image = pygame.transform.scale(star, (10, 13))

    def __init__(self, group):
        super().__init__(group)
        self.image = Star.image
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 450)
        self.rect.y = -70
    
    def update(self):
        v = 600
        fps = 100
        self.rect.y += v / fps
        if int(self.rect.y) == 400:
            self.kill() 
        clock.tick(fps)
        

class Star2(pygame.sprite.Sprite):  
    star = load_image("star2.png")
    image = pygame.transform.scale(star, (5, 5))

    def __init__(self, group):
        super().__init__(group)
        self.image = Star.image
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 450)
        self.rect.y = -70
    
    def update(self):
        v = 100
        fps = 100
        self.rect.y += v / fps
        clock.tick(fps)


all_sprites = pygame.sprite.Group()
v = 200
fps = 100
Wall(all_sprites)
My_ship(all_sprites)
Star(all_sprites)
Star2(all_sprites)
Rocket(all_sprites)
Enemy_ship(all_sprites)
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
timershowstar = 0
timershowstar2 = 0
rockettime = 0
running = True
while running:
    #print(shipposx)
    fps = int(clock.tick(fps))
    timershowstar += fps
    timershowstar2 += fps
    rockettime += fps
    # print(fps)
    # print(timershowstar)
    if timershowstar > 3000 and  timershowstar < 3200:
        timershowstar = 0 
        Star(all_sprites)
    if timershowstar2 > 4000 and  timershowstar2 < 4200:
        timershowstar2 = 0 
        Star2(all_sprites)  
    if rockettime > 2000 and rockettime < 2200:
        rockettime = 0
        Rocket(all_sprites)     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
pygame.quit()
