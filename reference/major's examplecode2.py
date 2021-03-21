import turtle as t
import random
import shapely
import pandas as pd

from shapely.geometry import Point, LineString, Polygon
from shapely.geometry import MultiLineString, MultiPolygon
from shapely.ops import unary_union, nearest_points
from matplotlib import pyplot, rcParams
from math import sin, cos, pi

# set parameters
score = []
tscore = pd.DataFrame()
myworld = Polygon([(-500, -500), (500, -500), (500, 500), (-500, 500)])     # 넓은 구역
mypoly = Polygon([(0, 0), (100, 0), (100, 100), (200, 100), (200, 200), (0, 200)])     # 설치 영역
weak1 = Polygon([(45, 95), (55, 95), (55, 105), (45, 105)])   # 취약지점1 설정
weak2 = Polygon([(145, 145), (145, 155), (155, 155), (155, 145)])   # 취약지점2 설정
weak3 = Polygon([(145, 45), (145, 55), (155, 55), (155, 45)])   # 취약지점2 설정
ant = 0

while ant < 50:             # 개미의 마릿수
    # 초기화 값
    totalview =Polygon()
    coverratio = 0
    kth = 0
    trith = 0
    while  kth < 5:               # 개미 한마리의 종결 조건
        # 카메라 포지션 랜덤 추출
        x = random.randint(0,300)
        y = random.randint(0,300)
        seta = random.randint(0, 360)          #회전을 무작위로(1도 단위)
        
        if Polygon(mypoly).contains(Point(x, y)):
            cL=int(200)                             #도형크기는 80
            
            # 삼각형들의 좌표를 뽑자. 
            pt0 = (x, y)                                                  # 삼각형 꼭지점 0
            pt1 = (x+(cL*cos(pi/3+seta)), y+(cL*sin(pi/3+seta)))         # 삼각형 꼭지점 1
            pt2 = (x+(cL*cos(pi*2/3+seta)), y+(cL*sin(pi*2/3+seta)))     # 삼각형 꼭지점 2
            # kth(k번째) 삼각형을 저장하자.         
            globals()['tri{}'.format(kth)] = Polygon([(pt0), (pt1), (pt2)])
            kth = kth + 1
            totalview = totalview.union(globals()['tri{}'.format(trith)])
            trith = trith + 1                    # 시도횟수(카메라 대수)
            intersect = totalview.intersection(mypoly)
            blind = mypoly.difference(totalview)
            worldblind = myworld.difference(totalview)
            distanceA = worldblind.distance(weak1)
            distanceB = worldblind.distance(weak2)
            distanceC = worldblind.distance(weak3)
            globals()['totalview{}'.format(ant+1)] = totalview
            coverratio = intersect.area/mypoly.area
            globals()['intersect{}'.format(ant+1)] = intersect
            globals()['blind{}'.format(ant+1)] = blind
            globals()['worldblind{}'.format(ant+1)] = worldblind
            globals()['distanceA{}'.format(ant+1)] = distanceA
            globals()['distanceB{}'.format(ant+1)] = distanceB
            globals()['distanceC{}'.format(ant+1)] = distanceC


            
    # kth를 score list에 저장
    ant = ant + 1
    score.append({ant, kth, coverratio, distanceA})
    kscore = pd.DataFrame({"개미번호" : [ant], "카메라댓수" : [kth], "커버율" : [coverratio], "최소탐지거리A" : [distanceA], "최소탐지거리B" : [distanceB], "최소탐지거리C" : [distanceC]})
    tscore = tscore.append(kscore)

    

tscore = tscore.reset_index(drop=True)
best_score = tscore.sort_values(by=['카메라댓수', '커버율'], axis=0, ascending=[True, False])
best_score = best_score.reset_index(drop=True)
best_score
selection = best_score.iloc[0,0]
min_number = best_score.iloc[0,1]
print(min_number)
globals()['intersect{}'.format(selection)]