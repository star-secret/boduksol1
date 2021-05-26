import pygame
import random
import sys

def paintEntity(entity,x,y):
    monitor.blit(entity,(x,y))

def playGame():
    global monitor,drone
    
    r= random.randrange(0,256)
    g= random.randrange(0,256)
    b= random.randrange(0,256)
    


    drone = pygame.image.load(random.choice(droneImage))
    droneSize = drone.get_rect().size
    droneX = 0
    droneY = random.randrange(0,int(swidth * 0.3))
    droneSpeed = random.randrange(1,5)

    while True:
        pygame.time.Clock().tick(50)
        monitor.fill((r,g,b))

        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
            
        droneX += droneSpeed
        if droneX > swidth:
            droneX = 0
            droneY = random.randrange(0,int(swidth * 0.3))
            drone = pygame.image.load(random.choice(droneImage))
            droneSize = drone.get_rect().size
            droneSpeed = random.randrange(1,5)

        paintEntity(drone,droneX,droneY)

        pygame.display.update()

r,g,b = [0] * 3
swidth,sheight = 500,700
droneImage=['blackdrone.png','triangl2.png']
drone = None

pygame.init()
monitor = pygame.display.set_mode((swidth,sheight))

playGame()