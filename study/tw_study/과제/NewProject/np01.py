import pygame, sys
from pygame.locals import *

pygame.init()

#디스플레이 설정
DISPLAYSURF = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption("Drawing")

#색깔 설정 - 화면에 그리려면 무슨색으로 그릴지 정해야 한다.
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#디스플레이 객체위에다 그리기
DISPLAYSURF.fill(WHITE) #배경을 하얀색으로 채움 .fill()은 객체의 메소드다
pygame.draw.polygon(DISPLAYSURF, GREEN,((146,0), (291,106), (236,277), (56,277), (0,106)))  
        #다각형을 어디에 그릴건지, 무슨색으로 그릴건지,꼭짓점은어디인지, 그려지는 선의 두께 이렇게 총 4가지를 인자로 받을 수 있다
        #여기서는 두께는 설정하지 않음
        #두께를 설정하지 않을경우 다각형 내부를 넘겨받은 인자의 색으로 채움
        #두께를 설정할 경우 다각형 내부는 색을 칠하지 않고 테두리만 색을 칠함
 
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))
        #이 직사각형의 인자를 해석하면, (200,150)의 위치에 직사각형의 좌측 상단이 그려진다
                                    # (200,150)을 기준으로 x축방향으로 +100, y축 방향으로 +50만큼 더해진 곳에 직사각형의 우측 하단이 그려진다

'''
pixObj = pygame.PixelArray(DISPLAYSURF)     단 하나의 픽셀에 색깔을 지정하기 위한 방법
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj
'''

while True:

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()

    pygame.display.update()     #이것을 호출해야 디스플레이에 우리가 그린 것들이 보여진다