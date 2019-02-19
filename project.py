import os
import pygame
from random import randint

pygame.init()
size = (400, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
# shipposx = 0
# rocketposx = 0
# rocketposy = 0
# enemyshipposx = 0
# enemyshipposy = 0
# timeboom = 0

Rockets = pygame.sprite.Group()
Enemy_ships = pygame.sprite.Group()
Enemy_ships2 = pygame.sprite.Group() 
vertical_borders = pygame.sprite.Group()

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

class Border(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.add(vertical_borders)
        self.rect = pygame.Rect(400, 0, 400, 500)

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
        if self.rect.x < 0:
            self.rect.x = -self.rect.x
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.rect.x = 355
                
class Enemy_ship(pygame.sprite.Sprite):  
    star = load_image("car2.png")
    boom = load_image("boom.png")
    boom_image = pygame.transform.scale(boom, (50, 50))
    image = pygame.transform.scale(star, (50, 50))

    def __init__(self, group):
        super().__init__(group)
        self.image = Enemy_ship.image
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 350)
        self.rect.y = -50
        self.destroyedat_y = 0
        self.delaytodisappear_y = 0
    
    def update(self):
        v = 100
        fps = 100
        self.rect.y += v / fps
        if pygame.sprite.spritecollideany(self , Rockets):
            self.destroyedat_y = self.rect.y
            self.delaytodisappear_y += v / fps
            self.image = self.boom_image
            if int(self.delaytodisappear_y) >= 10:
                self.kill()

class Enemy_ship2(pygame.sprite.Sprite):  
    star = load_image("car3.png")
    boom2 = load_image("boom.png")
    boom_image2 = pygame.transform.scale(boom2, (50, 50)) 
    image = pygame.transform.scale(star, (50, 50))

    def __init__(self, group):
        super().__init__(group)
        self.image = Enemy_ship2.image
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 350)
        self.rect.y = -50
        self.destroyedat_y = 0
        self.delaytodisappear_y = 0
    
    def update(self):
        v = 200
        fps = 100
        self.rect.y += v / fps
        if pygame.sprite.spritecollideany(self , Rockets):
            self.destroyedat_y = self.rect.y
            self.delaytodisappear_y += v / fps
            self.image = self.boom_image2
            if int(self.delaytodisappear_y) >= 20:
                self.kill() 

class Rocket(pygame.sprite.Sprite):
    Lazer = load_image("rocket.png")
    image = pygame.transform.scale(Lazer, (10, 25))

    def __init__(self, group):
        super().__init__(group)
        self.image = Rocket.image
        self.rect = self.image.get_rect()
        self.rect.x = My_ship.possition + 20
        self.rect.y = 395
        self.add(Rockets)
    
    def update(self):
        v = 300
        fps = 100
        self.rect.y -= v / fps
        if self.rect.y <= 0:
            self.kill()

class Wall(pygame.sprite.Sprite):
    wall = load_image("space.png")
    image = pygame.transform.scale(wall, (400, 500))

    def __init__(self, group):
        super().__init__(group)
        self.image = Wall.image
        self.rect = self.image.get_rect()  

class Star2(pygame.sprite.Sprite):  
    star2 = load_image("star2.png")
    image = pygame.transform.scale(star2, (7, 10))

    def __init__(self, group):
        super().__init__(group)
        self.image = Star2.image
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 450)
        self.rect.y = -70
    
    def update(self):
        v = 400
        fps = 100
        self.rect.y += v / fps
        #clock.tick(fps)

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
        v = 800
        fps = 100
        self.rect.y += v / fps
        
all_sprites = pygame.sprite.Group()
v = 200
fps = 0
Wall(all_sprites)
My_ship(all_sprites)
Star(all_sprites)
Star2(all_sprites)
Rocket(all_sprites)
Enemy_ship(all_sprites)
Enemy_ship2(all_sprites)
Border(vertical_borders)
start_ticks = pygame.time.get_ticks()
timershowstar = 0
timershowstar2 = 0
rockettime = 0
enemyship2time = 0
enemyshiptime = 0
running = True
while running:
    fps = int(clock.tick(fps))
    timershowstar += fps
    timershowstar2 += fps
    rockettime += fps
    enemyship2time += fps
    enemyshiptime += fps
    if timershowstar > 3000 and  timershowstar < 3200:
        timershowstar = 0 
        Star(all_sprites)
    if timershowstar2 > 4000 and  timershowstar2 < 4200:
        timershowstar2 = 0 
        Star2(all_sprites)  
    if rockettime > 1700 and rockettime < 1800:
        rockettime = 0
        Rocket(all_sprites)     
    if enemyship2time > 4000 and enemyship2time < 4100:
        enemyship2time = 0
        Enemy_ship2(all_sprites)
    if enemyshiptime > 4500 and enemyshiptime < 4550:
        enemyshiptime = 0
        Enemy_ship(all_sprites)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
pygame.quit()
