import numpy as np
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
