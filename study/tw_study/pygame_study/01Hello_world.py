import pygame, sys          #pygame과 sys 모듈을 가져와서 프로그램이 모듈 안의 함수를 사용할 수 있도록 함
from pygame.locals import * #pygame.locals에 대해서는 import형식을 다르게 해서 사용.
                            #from modulename import * 를 이용하면 module안의 변수나 함수를 이용할때 modulename을 쓸 필요가 없다
#1 게임 초기화
pygame.init()       #pygame 모듈을 가지고온 다음 pygame함수를 호출하기 전에 반드시 수행해야하는 함수로 게임초기화 역할을 담당

#2 게임창 옵션 설정 - 디스플레이
DISPLAYSURF = pygame.display.set_mode((400,300))    #pygame.display.set_mode가 반환하는 Surface객체는 display Surface
                                #set_mode()함수 안에 무조건 리스트와 튜플자료형을 이용하여서 가로 세로 한 쌍을 넘겨줘야함

#2 게임창 옵션 설정 - 제목
pygame.display.set_caption('Hello World!')          # 캡션설정 - 창의 이름을 설정

#4메인 이벤트
while True: 
    # 각종 입력 감지
    for event in pygame.event.get():            #pygame.event.get()은 pygame.event.Event 객체의 목록을 반환
                            #pygame.even.Event 목록은 프로그램이 시작한 다음 발생한 모든 이벤트들 (실시간으로 입력받아서 그걸 event에 넘겨주는거)
        
        if event.type ==QUIT:           #넘겨받은 객체의 type이 QUIT인지 판단
                        #pygame.locals.QUIT이지만 from pygame.locals import*를 이용했기 때문에 QUIT만 적어도 된다.
            pygame.quit()   #pygame라이브러리를 종료 (pygame관련 모듈을 이용하기 위한 자원을 해제)
            sys.exit()          #프로그램을 바로 종료 pygame.quit()만 있으면 정상적으로 종료가 안된다.

        #그리기
     
        #업데이트
    pygame.display.update   ##pygame.display.set_mode가 반환하는 Surface객체는 display Surface 객체 위에 그려진 어떤 것이라도 윈도우에 보여짐