import coordinate_split as sc

exit = 0
def left_discrimination(x1, y1, x2, y2, x, y):
    if ((y-y1)*(x2-x1)==(x-x1)*(y2-y1)):
        global exit
        exit+=1
        return 0
    if (x - x1 - (y - y1) * (x2 - x1) / (y2 - y1) < 0):
        return 1
    else:
        return 0

def inner_discrimination(area_of_interest_list, sensor_position_list, area_of_interest_xy, sensor_position_list_xy):
    interest_list = area_of_interest_list
    interest_xy = area_of_interest_xy
    sensor_pos = sensor_position_list
    sensor_pos_xy = sensor_position_list_xy
    sc.split_coord1(interest_list, interest_xy)
    sc.split_coord1(sensor_pos, sensor_pos_xy)

    global count
    global exit
    exit = 0

    for i in sensor_pos_xy:
        count = 0
        for j in range(len(interest_xy)):
            if(j == len(interest_xy)-1):
                if (interest_xy[j][1] <= i[1] <= interest_xy[0][1]) or (
                        interest_xy[j][1] >= i[1] >= interest_xy[0][1]):
                    if left_discrimination(interest_xy[j][0], interest_xy[j][1], interest_xy[0][0], interest_xy[0][1], i[0], i[1]) == 1:
                        count = count + 1
            #            print('b')

            else:
                if (interest_xy[j][1] <= i[1] <= interest_xy[j + 1][1]) or (
                        interest_xy[j][1] >= i[1] >= interest_xy[j + 1][1]):
                    if left_discrimination(interest_xy[j][0], interest_xy[j][1], interest_xy[j + 1][0], interest_xy[j + 1][1], i[0], i[1]) == 1:
                        count = count + 1

    #print('카운트:'+str(count))
    #print('익시트:' + str(exit))
    #print('배열길이:'+str(len(interest_xy)))
    if exit != 0:
       #print('경계면')
       #print('센서가 관심영역 밖에 있습니다')
       return 1

    if count % 2 == 0:
        #print('센서가 관심영역 밖에 있습니다')
        return 1
    else:
        #print('센서가 배치되었습니다.')
        return 2