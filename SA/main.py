import convert_png as cp
import make_sensor as msp
import save_png as spm
import split_coordinate as sc
import move_coordinate as mc
import move_change
import random_move
import numpy as np
from random import *

"""

#변하지 않는 값
total_pixel_of_interest = 100000
#area_of_interest_list = []
'''
area_of_interest_list.append((286,39))
area_of_interest_list.append((515,408))
area_of_interest_list.append((58,410))
'''
area_of_interest_list = []
sc.split_coord1(input("관심영역의 좌표를 입력하시오.").split(' '), area_of_interest_list) #관심영역 좌표 리스트
print(area_of_interest_list)
detect_range = int(input("센서의 탐지범위를 입력하시오.\n")) #센서 탐지범위

#변하는 값(초기값)
sensor_number = 6 #센서 갯수 -> 추후 변경
max_coverage_percent = 0 #가장 큰 커버율 -> 이 커버율이 100퍼센트가 되면 종료
max_coverage_percent_section = 0 #section의 커버율이


#코드 진행
basic_png = spm.start(area_of_interest_list,[],detect_range)
basic_png.save_png()
cp.convert("image_test0.png", total_pixel_of_interest)

#boundary_list = sa.splitList(sa.getContour(sensor_number))

#print(boundary_list)
'''
for i in boundary_list:
    for k in range(0,sensor_number):
        #"area" + str(k) = msp.area(i)

#areak.propercordinate()

sensor_list = areak.makearea()
while(max_coverage_percent != 100):
    for i in sensor_list:

    break


#sensor_position_list = []
#sensor_position_list = 어떤 애가 sensor 위치 무작위로 배열하는 그런게 있겠지 업데이트 될 듯

#구간을 나누고
#반복문 하나 돌때마다 나누는 갯수를 늘려
#구간 나누는 함수가 필요하고

#a = sl.sel(area_of_interest_list, sensor_position_list, area_of_interest_list_xy, sensor_position_list_xy)
#a.inner_discrimination()  #이 값이 1을 return 하면 그대로 가는거고 이 값이 2를 return하면 다시 loop를 돌게끔 해야함



#cp.convert("image_test0.png",total_pixel_of_interest)
#cp.convert("image_test1.png",total_pixel_of_interest)



"""

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
    print("센서:")
    print(sensor)
    tempsensor = mc.move_coordinate(sensor,tempmove)
    print("temp센서:")
    print(tempsensor)

    basic_png.change_sensor(sensor)
    print(sensor)
    basic_png.save_png()
    count+=1
    obj = cp.convert_return_count("image_test"+str(count)+".png")
    print(obj)
    objportion = cp.convert_return_portion(obj, total_pixel_of_interest)
    print(str(count)+". objportion:"+str(objportion))

    basic_png.change_sensor(tempsensor)
    print(tempsensor)
    basic_png.save_png()
    count+=1
    tempobj = cp.convert_return_count("image_test"+str(count)+".png")
    tempobjportion = cp.convert_return_portion(tempobj, total_pixel_of_interest)
    print(tempobj)
    print(str(count)+". tempobjportion:"+str(tempobjportion))

    if np.exp((tempobj-obj)/T)>random():
        print("exp:")
        print(round(np.exp(-(tempobjportion-objportion)/T),5))
        sensor = tempsensor
        move = tempmove
        tempmove = move_change.random_nextMove_change1(move)
        param = 1
    else:
        param = 0
    T=T-0.05

print(obj)


"""
#변하지 않는 값
area_of_interest_list = []
sc.split_coord1(input("관심영역의 좌표를 입력하시오.").split(' '), area_of_interest_list) #관심영역 좌표 리스트
#입력 예시 지금은 정삼각형만 입력해야함 (200,200) (600,200) (400,540)           // (286,39) (515,408) (58,410)
detect_range = int(input("센서의 탐지범위를 입력하시오.\n")) #센서 탐지범위

basic_png = sp.start(area_of_interest_list,[],detect_range)
basic_png.save_png()
total_pixel_of_interest = cp.convert_return_count("image_test0.png")
"""