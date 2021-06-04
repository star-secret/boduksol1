import warnings
import numpy as np
import cv2
import pandas as pd
import math
import random as rd


def point2D(hakx, haky, conta, contb):
    a = hakx - conta
    b = haky - contb
    c = math.sqrt((a * a) + (b * b))
    return c


def getCenter():
    img = cv2.imread('sample.png')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contours_list = contours[0].flatten().reshape(-1, 2).tolist()
    contours_list = contours_list[::20][:]
    contour_x = 0
    contour_y = 0
    for i in range(len(contours_list)):
        contour_x += (contours_list[i][0])
        contour_y += (contours_list[i][1])
    center_x = int(contour_x / len(contours_list))
    center_y = int(contour_y / len(contours_list))
    centerlist = [center_x, center_y]
    return centerlist


# center의 좌표를 리스트로 return하기 추가
'''
    contour = contours[0]
    leftmost = tuple(contour[contour[:,:,1].argmin()][0])
    최북단 점 찾기
'''


def getContour(dotNum):
    img = cv2.imread('sample.png')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contours_list = contours[0].flatten().reshape(-1, 2).tolist()
    randnum = int(rd.randint(0, 5) + (len(contours_list) / dotNum))
    contours_list = contours_list[::randnum][:]
    return contours_list


def splitList(contours_list):  # list별로 영역 나누기
    center = getCenter()
    dot1 = [286, 39]
    dot2 = [515, 408]
    dot3 = [58, 410]
    contours_list.insert(0, [dot1])
    contours_list.insert(3, [dot2])
    contours_list.insert(6, [dot3])
    contours_list.insert(9, [dot1])
    list1 = contours_list[1:3] + [center]
    list2 = contours_list[2:5] + [center]
    list3 = contours_list[4:6] + [center]
    list4 = contours_list[5:8] + [center]
    list5 = contours_list[7:9] + [center]
    list6 = contours_list[8:] + [center]  # 이부분 어떻게 좀 보기좋게 수정하남..

    return list1, list2, list3, list4, list5, list6


splitList(getContour(6))

'''
    for i in range(len(contours_list)):

        print([contours_list[:]0]], contours_list[i][0])
'''

'''
img = cv2.imread('pic.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thr = cv2.threshold(imgray, 127, 255, 0)
contours, _ = cv2.findContours(thr, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours_list = contours[0].flatten().reshape(-1,2).tolist()
contours_list = contours_list[::20][:]

cv2.drawContours(img, contours, -1, (255,0,0), 1)
cv2.imshow('thresh',thr)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
'''