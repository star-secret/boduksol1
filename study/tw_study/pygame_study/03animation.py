import pygame, sys

from pygame.locals import *

pygame.init()


FPS = 60 # 초당 프레임 수 : 1초당 30개의 이미지

fpsClock = pygame.time.Clock()  #pygame.time.Clock()객체는 우리 프로그램이 최대의 FPS로 동작할 수 있도록 한다
                                #Clock 객체는 게임 루프를 돌 때 약간씩 간격을줘서 프로그램이 너무빨리 수행되지 않게 한다
                                #얼마나 간격을 줄 지는 tick()을 호출한 다음 얼마나 시간이 지났는지에 따라 계산해서 수행
                                #게임 루프의 주기 결정

#윈도우 설정
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')


WHITE = (255, 255, 255)

catImg = pygame.image.load('cat.png')   #'cat.png'이미지를 그릴 pygame.Surface객체를 반환해서 catImage에 저장
                                        #pygame.display.set_mode에서 반환한 디스플레이용 pygame.Surface객체와는 다른 객체
                                        #이미지용 Surface객체이다
                                        #이미지를 불러오기 위해서는 이 파일이 .py파일이 실행되는 위치에 있어야 한다.
catx = 10
caty = 10
direction = 'right'


while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5

        if catx == 280:
            direction = 'down'

    elif direction == 'down':
        caty += 5

        if caty == 220:
            direction = 'left'

    elif direction == 'left':
        catx -= 5

        if catx == 10:
            direction = 'up'

    elif direction == 'up':
        caty -= 5

        if caty == 10:
            direction = 'right'


    DISPLAYSURF.blit(catImg, (catx, caty))     #blit()메소드를 이용하여 catImage라는 Surface객체를 디스플레이Surface개체에 그릴 수 있게함
                                               #한 Surface객체의 내용을 다른 Surface 객체 위에 그림
                                               #두번째 인자는 객체가 복사될 때 객체가 위치할 왼쪽 ㅏㅇ단의 좌표이다

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()

    fpsClock.tick(FPS)          #이 코드가 무조건 있어야 하는데, 아직까지는 왜 있어야 하는지 잘 이해가 되지 않는다.