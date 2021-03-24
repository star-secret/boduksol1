import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

clock = pygame.time.Clock()

done=True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pixel_col = (randint(0,255),randint(0.255),randint(0,255))

    screen.lock()
    for i in range(30):
        pixel_pos = (randint(0,639),randint(0.479))
        screen.set_at(pixel_pos,pixel_col)
    screen.unlock()
    pygame.display.update()

    clock.tick(10)

pygame.display.quit()