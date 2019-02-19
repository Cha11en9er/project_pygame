import sys, pygame, os, math
from random import randint

pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 1, 1, 1
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pick up the squares!')
UP='up'
DOWN='down'
LEFT='left'
RIGHT='right'

ball = pygame.image.load("car2.png")
ballrect = ball.get_rect()
ballx = 400
bally = 300

blip = pygame.image.load("rocket.png")
bliprect = blip.get_rect()
blipx = randint(1,300)
blipy = randint(1,300)

background = pygame.Surface(screen.get_size())
background = background.convert()

background.fill((250, 250, 250))


clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ballx  -= 5
    if keys[pygame.K_RIGHT]:
        ballx += 5
    if keys[pygame.K_UP]:
        bally -= 5
    if keys[pygame.K_DOWN]:
        bally +=5    

    screen.fill(black)
    screen.blit(ball, (ballx,bally))
    screen.blit(blip, (blipx, blipy))
    pygame.display.update()
    clock.tick(40)