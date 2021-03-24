import pygame
import sys



SCREEN=(500,500)
screen = pygame.display.set_mode(SCREEN,pygame.RESIZABLE)
pygame.display.set_caption('창크기:'+str(SCREEN))
screen.fill((0,0,255))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:

            NAJUNG_SCREEN = event.size
            screen = pygame.display.set_mode(NAJUNG_SCREEN,pygame.RESIZABLE)

            pygame.display.set_caption('창크기:'+str(SCREEN)+'=>'+str(NAJUNG_SCREEN))

            screen.fill((0,0,255))
            pygame.display.update()

            SCREEN=NAJUNG_SCREEN