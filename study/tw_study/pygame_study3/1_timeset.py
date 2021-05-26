import sys,pygame
from pygame.locals import *

pygame.init()
size=(1024,768)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
fontObj = pygame.font.Font(None, 32)
counter = 0

running = True  
while running:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    counter +=1
    screen.fill((0,0,0))
    count_image = fontObj.render("count is{}".format(counter), True, (225,225,225))
    screen.blit(count_image,(50,50))
    pygame.display.update()
    dt = clock.tick(1)
        