#입력예시
#

length = 10
def move_coordinate(sensor_coordinate, movenum):
    i = sensor_coordinate
    if movenum == 1:
        i[0] = i[0] + length
        i[1] = i[1] + length
    elif movenum == 2:
        i[0] = i[0] + length
    elif movenum == 3:
        i[0] = i[0] + length
        i[1] = i[1] - length
    elif movenum == 4:
        i[1] = i[1] - length
    elif movenum == 5:
        i[0] = i[0] - length
        i[1] = i[1] - length
    elif movenum == 6:
        i[0] = i[0] - length
    elif movenum == 7:
        i[0] = i[0] - length
        i[1] = i[1] + length
    elif movenum == 8:
        i[1] = i[1] + length


    return sensor_coordinate