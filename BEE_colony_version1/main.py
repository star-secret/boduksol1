import save_png as sp
import make_coord as mc
import split_coordinate as sc

area_of_interest = input("관심영역의 좌표를 입력하시오.").split(' ')
# 입력예시 x,y x2,y2 x3,y3
# 입력예시 0,0 0,4 4,4 4,0
cordxlist = []
cordylist = []
sensornumber = 3
colony_number = 10
detect_range = 90
area_of_interest_list =[]

################################################################

for i in area_of_interest:
    area_of_interest_split = i.split(',')
    cordxlist.append(area_of_interest_split[0])
    cordylist.append(area_of_interest_split[1])

#군집 n개 만들기
colonylist = []

for i in range(0, colony_number):
    test = []
    for j in range(sensornumber):
        k = mc.make_coord(test, cordxlist, cordylist)

    colonylist.append(k)

sc.split_coord1(area_of_interest, area_of_interest_list)
spa = sp.start(area_of_interest_list, colonylist[0], detect_range)

for i in range(0, 10):
    spa = sp.start(area_of_interest_list, colonylist[i], detect_range)

    #globals()['sp'.format(i)] = sp.start(area_of_interest_list, colonylist[i], detect_range)



#sp.start()
