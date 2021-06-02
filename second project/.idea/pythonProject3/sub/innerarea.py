import time
import threading
from PIL import Image
import numpy as np
import glob
import time
import pygame
from pygame.locals import *
import cv2

def convert(filename): #파일이 주어지면 비율계산
    img = cv2.imread(filename) #파일 불러오기
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #흑백으로 변환

    ret, thr = cv2.threshold(imgray, 127, 255, 0) #흑(0) 또는 백(1)으로 변환
    imnp = np.array(thr)
    h, w = imnp.shape[:2] #높이와 너비 변수에 대입

    colors, counts = np.unique(imnp.reshape(-1,1), axis=0, return_counts=1) #현재 배열은 0또는 1값을 가지는데, 0의 개수와 1의 개수를 세서 counts에 기록
    count = counts[0] #이를 count에 대입 counts[0]은 0의 개수, counts[1]은 1의 개수
    portion = (count)*100/330600 #330600은 현재 주어진 관심범위의 픽셀값. 변수로 입력받기 필요할듯
    print(count)
    print(f"{portion:.2f}%") #비율출력





# screensize=(1600,900)
# gwansim = [(300,300),(1400,700),(1500,900),(500,800)]
# radarxy=[(200,200),(800,500),(500,800)]
# radar_range=300
# WHITE = (255,255,255)
# BLACK = (0,0,0)
# YELLOW = (255,255,0)


# pygame.init()
# screen = pygame.display.set_mode(screensize)
# screen.fill(WHITE)
# radius=0
# done = True

# while done:
#    for event in pygame.event.get():
#         if event.type == QUIT:
#             done = False

#    pygame.draw.polygon(screen,BLACK,gwansim)
#    for i in range(len(radarxy)):
#        pygame.draw.circle(screen, YELLOW, radarxy[i], radar_range)

#    pygame.image.save(screen, repr(radius) + "1.jpg")

#    pygame.display.update()

# pygame.display.quit()
#    #yeonyeokgubun()


# def screenshot_persec(k):
#     img = cv2.imread('my_region_{}.png'.format(k))
#     imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     ret, thr = cv2.threshold(imgray, 127, 255, 0)
#     cv2.imshow('thresh',thr)
#     cv2.waitKey()
#     cv2.destroyAllWindows()



# def processLog(filename):
#     print(f"Processing log: {filename}")
#     # Open this image and make a Numpy version for easy processing
#     im   = Image.open(filename).convert('RGBA').convert('RGB')
#     imnp = np.array(im)
#     imnp = imnp[::2]
#     h, w = imnp.shape[:2]
#     # Get list of unique colours...
#     # Arrange all pixels into a tall column of 3 RGB values and find unique rows (colours)
#     colours, counts = np.unique(imnp.reshape(-1,3), axis=0, return_counts=1)
#     # Iterate through unique colours
#     #[(255,255,255),(23,52,14),...] [59999, 244, ...]
#     for index, colour in enumerate(colours):
#         count = counts[index]
#         proportion = (100 * count) / (h* w)
#         if(count<=200):
#             continue
#         print(f"   Colour: {colour}, count: {count}, proportion: {proportion:.2f}%")


# time.sleep(3)

# start = time.time()  # 시작 시간 저장
# for i in range(10):
#     screenshot_persec(i)
#     processLog('my_region_{}.png'.format(i))
# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간