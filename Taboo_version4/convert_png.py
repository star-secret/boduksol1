import numpy as np
import cv2

#저장된 사진으로 커버율을 계산하는 함수

#관심영역의 색상은 어두운 색상으로 할것. 검은색으로
#레이더의 색상은 밝은 색상으로 할것. 흰색으로

def convert(filename, area_interest): #파일이 주어지면 비율계산
    img = cv2.imread(filename) #파일 불러오기
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #흑백으로 변환

    ret, thr = cv2.threshold(imgray, 127, 255, 0) #흑(0) 또는 백(1)으로 변환
    imnp = np.array(thr)
    h, w = imnp.shape[:2] #높이와 너비 변수에 대입

    colors, counts = np.unique(imnp.reshape(-1,1), axis=0, return_counts=1) #현재 배열은 0또는 1값을 가지는데, 0의 개수와 1의 개수를 세서 counts에 기록
    count = counts[0] #이를 count에 대입 counts[0]은 0의 개수, counts[1]은 1의 개수
    portion = (1-((count)/area_interest))*100 #area_interest에는 주어진 관심영역의 픽셀값이 들어가야함!
    print(count)
    print(f"{portion:.2f}%") #비율출력

#convert("sample.png", 100000)