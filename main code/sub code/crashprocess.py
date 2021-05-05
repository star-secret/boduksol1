import pygame
import os
from PIL import Image
import numpy as np
import time
from pygame.locals import*
import cv2

haeksim=(500,500)
gwansimsize=(800,800)
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(180,160,150)
radarxy=[]
radar_range=[]
INIT = 0
#컬러에서 흑백 변환 원리 : (R+G+B)/3

def processLog(filename):
    sum=0
    print(f"Processing log: {filename}")
    im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    ret, thr1 = cv2.threshold(im, 200, 225, cv2.THRESH_BINARY)
    imnp = np.array(thr1)
    h, w = imnp.shape[:2]
    colours, counts = np.unique(imnp.reshape(-1, 1), axis=0, return_counts=1)

    for index, colour in enumerate(colours):
        count = counts[index]
        if (colour[0]<2):
            sum+=count
    return sum

radarxy.append((400,400))
radar_range.append(160)

pygame.init()
screen = pygame.display.set_mode(gwansimsize)
screen.fill((255,255,255))
radius=0
done = True

while done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = False
    for i in range(len(radarxy)):
        pygame.draw.circle(screen, BLUE,radarxy[i],radar_range[i])

    pygame.draw.circle(screen, BLACK, haeksim, radius)
    radius+=1
    pygame.image.save(screen, repr(radius)+".jpg")
    pygame.display.update()

    if INIT==0:
        BLACKPIXEL = processLog(repr(radius) + ".jpg")
        ORIGINAL_BLACKPIXEL = BLACKPIXEL
        INIT = INIT+1

    else:
        BLACKPIXEL = processLog(repr(radius) + ".jpg")
        if BLACKPIXEL == ORIGINAL_BLACKPIXEL:
            continue
        else:
            print(radius-1)
            break

time.sleep(3)
pygame.display.quit()