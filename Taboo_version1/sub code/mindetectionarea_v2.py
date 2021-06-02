import pygame
from PIL import Image
import numpy as np
from pygame.locals import*
import time
start = time.time()

haeksim=(500,500) #핵심시설의 좌표 지정
gwansimsize=(1920,1080) #관심영역의 크기 지정
WHITE = (255, 255, 255)  # 색깔정의
BLACK = (0, 0, 0)
radarxy = []
radar_range = []
INIT = 0
pygame.init()
screen = pygame.display.set_mode(gwansimsize)
screen.fill((255, 255, 255))


def processLog(filename):
    sum=0
    print(f"Processing log: {filename}")
    # Open this image and make a Numpy version for easy processing
    im = Image.open(filename).convert('RGBA').convert('RGB')
    imnp = np.array(im)
    imnp = imnp[::2]
    h, w = imnp.shape[:2]
    # Get list of unique colours...
    # Arrange all pixels into a tall column of 3 RGB values and find unique rows (colours)
    colours, counts = np.unique(imnp.reshape(-1, 3), axis=0, return_counts=1)
    # Iterate through unique colours

    for index, colour in enumerate(colours):
        count = counts[index]
        #if(count <= 200):
        #    continue
        if (colour[0]<2 and colour[1]<2 and colour[2]<2):
            sum+=count
    return sum

#def inputradar(*xy):
#    radarxy.append(xy)

#def inputrange(*range):
#    radar_range.append(range)


"""
while True:
    i = input("레이더의 좌표를 입력하시오.\n")
    if i=='end':
        break
    a = i.split(",")
    a[0]=a[0].replace('(','')
    a[1] =a[1].replace(')','')
    radarxy.append([int(a[0]),int(a[1])])
    b = int(input("레이더의 탐지범위를 입력하시오.\n"))
    radar_range.append(b)
"""
radarxy.append((400,400))
radar_range.append(160)

#def MinDetectionRadius():
WHITE = (255, 255, 255)  # 색깔정의
BLACK = (0, 0, 0)
INIT = 0
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
        pygame.draw.circle(screen, BLACK,radarxy[i],radar_range[i])

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
pygame.display.quit()