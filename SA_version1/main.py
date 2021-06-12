import convert_png as cp
import make_sensor as msp
import save_png as spm
import split_coordinate as sc
import move_coordinate as mc
import move_change
import random_move
import numpy as np
import copy
from random import *

sensorxy = []
T = 60
area_of_interest_list = []
sc.split_coord1(input("관심영역의 좌표를 입력하시오.").split(' '), area_of_interest_list) #관심영역 좌표 리스트
#입력 예시 지금은 정삼각형만 입력해야함 (200,200) (600,200) (400,540)           // (286,39) (515,408) (58,410)
print(area_of_interest_list)
detect_range = int(input("센서의 탐지범위를 입력하시오.\n")) #센서 탐지범위
#변하는 값(초기값)
sensor_number = 6
length = 9#move의 숫자열 길이
move = [] #예시=[[0,1,0,0,1,0,0,1,1],[1,0,0,1,0,0,1,0,1]]
tempmove = []
sensor = [] #예시=[[100,200],[200,300]]
tempsensor = []
param = 0
count = 0

#관심영역의 총 픽셀 계산
basic_png = spm.start(area_of_interest_list,[],detect_range)
basic_png.save_png()
total_pixel_of_interest = cp.convert_return_count("image_test0.png")

for i in range(sensor_number):
    sensor.append(msp.area(area_of_interest_list).propercordinate())

'''
print(sensor)

sensor = [[100,200],[200,300]]
tempsensor= [[200,100],[300,200]]


print(total_pixel_of_interest)


'''
basic_png.change_sensor(sensor)
basic_png.save_png()
count+=1
obj = cp.convert_return_count("image_test"+str(count)+".png")
objportion = cp.convert_return_portion(obj,total_pixel_of_interest)

for i in range(sensor_number):
    move.append([0,0,0,0,1,1,1,0,1])
    tempmove.append(random_move.create_move(length))

while T>=1:
    if param==1:
        sensor = mc.move_coordinate(sensor,move)
    #print("센서:")
    #print(sensor)
    basic_png.change_sensor(sensor)
    basic_png.save_png()
    count+=1
    obj = cp.convert_return_count("image_test"+str(count)+".png")
    #print(obj)
    objportion = cp.convert_return_portion(obj, total_pixel_of_interest)
    #print(str(count)+". objportion:"+str(objportion))

    #print("센서:")
    #print(sensor)
    tempsensor = copy.deepcopy(sensor)
    tempsensor = mc.move_coordinate(tempsensor,tempmove)
    #print("temp센서:")
    #print(tempsensor)
    #print("센서:")
    #print(sensor)
    basic_png.change_sensor(tempsensor)
    basic_png.save_png()
    count+=1
    tempobj = cp.convert_return_count("image_test"+str(count)+".png")
    tempobjportion = cp.convert_return_portion(tempobj, total_pixel_of_interest)
    #print(tempobj)
    #print(str(count)+". tempobjportion:"+str(tempobjportion))

    if np.exp(-(tempobjportion-objportion)/T)<=random():
        print("exp:")
        print(round(np.exp(-(tempobjportion-objportion)/T),5))
        sensor = copy.deepcopy(tempsensor)
        move = copy.deepcopy(tempmove)

        param = 1
    else:
        param = 0
    tempmove = move_change.random_nextMove_change1(move)
    T=T-0.05

print(obj)

