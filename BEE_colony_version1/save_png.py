import math, sys
import pygame
import time, random
from pygame.locals import *

# 함수화..

polygon_list = []
polygon_list.append([10, 10])
polygon_list.append([1200, 10])
polygon_list.append([1200, 700])
polygon_list.append([10, 700])

polygon_list2 = []
polygon_list2.append([10, 10])
polygon_list2.append([1200, 10])
polygon_list2.append([1200, 700])

sensor_list = []
sensor_list.append([100, 200])
sensor_list.append([400, 500])
radius = 30
version = 8


class start:

    def __init__(self, input_list, input_sensor, input_radius, input_version):  # version 입력받아야함, 니 i를 버전에다가 넣어주면 될듯?

        self.screen_size = (1360, 768)
        self.polygon = [] + input_list
        self.countpicture = 0
        self.sensor = [] + input_sensor
        self.sensor_radius = input_radius
        self.version = input_version  # 객체의 버전정보 저장

    def runGame(self, screen):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False

            pygame.draw.polygon(screen, (0, 0, 0), self.polygon)
            for number in self.sensor:
                pygame.draw.circle(screen, (180, 160, 100), number, self.sensor_radius, 0)
            pygame.display.update()
            pygame.image.save(screen, "image_test_version_ " + (str)(self.version) + ", number_" + (str)(
                self.countpicture) + ".png")  # 상태저장, 버전정보까지 아 콜론이 이미지 이름에 들어가니까 오류나더라 ㅅㅂ
            self.countpicture = self.countpicture + 1
            run = False
        pygame.quit()

    def change_polygon(self, input_list):
        self.polygon.clear()
        self.polygon = input_list

    def change_radius(self, input_radius):
        self.sensor_radius = input_radius

    def its_main(self):
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size, DOUBLEBUF)
        screen.fill((255, 255, 255))

        self.runGame(screen)


yeahgood = start(polygon_list, sensor_list, radius, version)

yeahgood.its_main()

yeahgood.change_polygon(polygon_list2)
yeahgood.change_radius(90)

yeahgood.its_main()

