import cv2


# 영역을 나누는 모듈

def getCenter(fname):
    img = cv2.imread(fname)
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


def getContour(dotNum,fname):
    img = cv2.imread(fname)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contours_list = contours[0].flatten().reshape(-1, 2).tolist()
    if(dotNum==3):
        contours_list = contours_list[200::int((len(contours_list) / dotNum))][:]
        return contours_list
    elif(dotNum==4):
        contours_list = contours_list[50::300][:]
        return contours_list
    elif(dotNum==5):
        contours_list = contours_list[120::200][:]
        return contours_list
    elif(dotNum==6):
        contours_list = contours_list[50::150][:]
        return contours_list
    elif(dotNum==7):
        contours_list = contours_list[140::140][:]
        return contours_list
    elif(dotNum==8):
        contours_list = contours_list[50::120][:]
        return contours_list
    elif(dotNum==9):
        contours_list = contours_list[50::100][:]
        return contours_list



def splitList(contours_list, dot_list,
            center, dot_number):  # list별로 영역 나누기,  [[286, 39],[515, 408],[58, 410]], center = getCenter()
    
    if(dot_number == 6):
        contours_list.insert(0, dot_list[0])
        contours_list.insert(2, dot_list[1])
        contours_list.insert(5, dot_list[2])
        contours_list.insert(8, dot_list[3])
        
        list1 = [contours_list[0]] + [contours_list[1]] + [contours_list[10]] + [center]
        list2 = [contours_list[1]] + [contours_list[2]] + [contours_list[3]] + [center]
        list3 = [contours_list[3]] + [contours_list[4]] + [center]
        list4 = [contours_list[4]] + [contours_list[5]] + [contours_list[6]] + [center]
        list5 = [contours_list[6]] + [contours_list[7]] + [center]
        list6 = [contours_list[7]] + [contours_list[8]] + [contours_list[9]] + [center]
        list7 = [contours_list[9]] + [contours_list[10]] + [center]
        spliced_list = [list1, list2, list3, list4, list5, list6, list7]

    return spliced_list