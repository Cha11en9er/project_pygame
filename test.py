# import os
# import pygame
# import random

# pygame.init()
# size = (400, 500)
# screen = pygame.display.set_mode(size)

# class Ball(pygame.sprite.Sprite):
#     def __init__(self, radius, x, y):
#         super().__init__(group)
#         self.radius = radius
#         self.image = pygame.Surface((2 * radius, 2 * radius),
#                                     pygame.SRCALPHA, 32)
#         pygame.draw.circle(self.image, pygame.Color("red"),
#                            (radius, radius), radius)
#         self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
#         self.vx = random.randint(-5, 5)
#         self.vy = random.randrange(-5, 5)
 
#     def update(self):
#         self.rect = self.rect.move(self.vx, self.vy)

# class Border(pygame.sprite.Sprite):
#     def __init__(self, x1, y1, x2, y2):
#         super().__init__(all_sprites)
#         if x1 == x2:  # вертикальная стенка
#             self.add(vertical_borders)
#             self.image = pygame.Surface([1, y2 - y1])
#             self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
#         else:  # горизонтальная стенка
#             self.add(horizontal_borders)
#             self.image = pygame.Surface([x2 - x1, 1])
#             self.rect = pygame.Rect(x1, y1, x2 - x1, 1)

# Border(5, 5, width - 5, 5)
# Border(5, height - 5, width - 5, height - 5)
# Border(5, 5, 5, height - 5)
# Border(width - 5, 5, width - 5, height - 5)

# all_sprites = pygame.sprite.Group()

# for i in range(10):
#     Ball(20, 100, 100)

# Ball(all_sprites)
# horizontal_borders = pygame.sprite.Group()
# vertical_borders = pygame.sprite.Group()

# running = True
# while running:  
#     all_sprites.draw(screen)
#     all_sprites.update()
#     pygame.display.flip()
# pygame.quit()




import os
import pygame
import random
from random import randint

pygame.init()
size = (600, 300)
Surface = pygame.display.set_mode(size)
radius = 50
x = randint(0, 300)
y = randint(0, 300)

class Bomb(pygame.sprite.Sprite):
    def __init__(self, group):
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)
 
    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            self.image = self.boob

all_sprites = pygame.sprite.Group()

for _ in range(20):
    Bomb(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False     
        Surface.fill((0, 0, 0))
        all_sprites.draw(Surface)
        all_sprites.update()
        pygame.display.flip()
pygame.quit()
