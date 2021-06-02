import math, sys
import pygame
import time, random
from pygame.locals import *

polygon_list = []
polygon_list.append([10, 10])
polygon_list.append([1200, 10])
polygon_list.append([1200, 700])
polygon_list.append([10, 700])

polygon_list2 = []
polygon_list2.append([10, 10])
polygon_list2.append([1200, 10])
polygon_list2.append([1200, 700])


class start:
    screen_size = (0, 0)

    def __init__(self, input_list):  # input_list로 이제 그릴거 입력받음
        self.screen_size = (1360, 768)
        self.polygon = [] + input_list
        self.countpicture = 0
        self.background = pygame.image.load('background1360768.png')

    def runGame(self, screen):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False

            pygame.draw.polygon(screen, (255, 255, 255), self.polygon, 5)  # polygon 그리기
            pygame.display.update()  # 화면 업데이트
            pygame.image.save(screen, "image_test" + (str)(self.countpicture) + ".png")
            self.countpicture = self.countpicture + 1
            run = False
        pygame.quit()

    def change_polygon(self, input_list):
        self.polygon.clear()
        self.polygon = input_list

    def save_png(self):  # 이 함수 호출하면 이제 죄다 실행되는거임
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size, DOUBLEBUF)
        screen.blit(self.background, (0, 0))
        self.runGame(screen)


yeahgood = start(polygon_list)  # 객체 생성

yeahgood.save_png()  # 이거 호출하면이제 그냥 리스트대로 화면 캡처하고 저장해줌

yeahgood.change_polygon(polygon_list2)  # 여기에다가 바꾼 리스트 넣으면 도형 바뀜

yeahgood.save_png()  # 바뀐고 보여줄려고 함수 호출한번 더함

yeahgood.change_polygon()

# input_list -> 관심 영역 좌표 고정이지() -> 정삼각형, 정사각형 이런거
# sensor_pos -> 그 좌표를 원의중심으로하는 원을그려야지, 좌표 리스트만 받을 수 있으면 됨
# r -> 센서 반지름이 다 동일해 