import pygame, sys
import random
from pygame.locals import *


pygame.init()
#화면 크기 설정
screen_width = 480   #가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Anti drone simulation")

#프레임설정
clock = pygame.time.Clock()

#하나의 드론 생성
bluedrone = pygame.image.load("bluedrone.png").convert_alpha()
#드론의 x,y값 랜덤
bd_x =random.randrange(0,480)
bd_y =random.randrange(0,640)



#메인루프
running =True
while running:
    #프레임 60
    clock.tick(60)
    for event in pygame.event.get():    #이벤트(마우스,키보드) 체크
        if event.type == pygame.QUIT:    #일반적인 창에 있는 x버튼을 눌렀을 때 발생하는 이벤트
            running = False     #게임 진행 중 아님
    #screen에 객체 표시
    screen.blit(bluedrone,(bd_x,bd_y))  

  



    #스크린 업데이트
    pygame.display.update()

pygame.quit()
sys.exit()
