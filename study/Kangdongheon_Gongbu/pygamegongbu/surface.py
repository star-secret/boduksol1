import pygame
from pygame.locals import*
from sys import exit

WIDTH=600
HEIGHT=400

pygame.init()

screen=pygame.display.set_mode([WIDTH,HEIGHT])

done=True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    red_rect = pygame.Rect(50,50,200,150)
    blue_rect = pygame.Rect(150,150,200,150)

    red_surface = screen.subsurface(red_rect)
    blue_surface = screen.subsurface(blue_rect)

    red_surface.fill((255,0,0))
    blue_surface.fill((0,0,255))

    red_surface=red_surface.copy()
    blue_surface=blue_surface.copy()

    screen.blit(red_surface,red_rect)
    screen.blit(blue_surface,blue_rect)
    screen.blit(red_surface, blue_rect)
    screen.blit(blue_surface, red_rect)

    pygame.display.update()

pygame.display.quit()

"""
import pygame

pygame.init()

width = 640
height = 480

WHITE=(255,255,255)
BLACK=(0,0,0)

screen=pygame.display.set_mode((width,height))

done=True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=False

    newSurface = pygame.Surface((int(width*0.8),int(height*0.8)))
    newSurface.fill(WHITE)

    screen.blit(newSurface,(int(width*0.1),int(height*0.1)))

    pygame.display.update()
pygame.display.quit()
"""
"""
import pygame
pygame.init()

pygame.display.set_mode((500,500))
abc = pygame.Surface((256,256))
pygame.Surface.fill(abc,(255,255,255))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
"""