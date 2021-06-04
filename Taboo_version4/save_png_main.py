import pygame
from pygame.locals import *

#관심영역 좌표, 센서 좌표, 센서 반지름 등을 받아서 사진으로 저장하는 함수 -> 커버율을 계산하기 위함임

class start:
    def __init__(self, input_list, input_sensor,
                 input_radius):  # input_list는 이제 관심영역 리스트 입력받는거, input_sensor는 센서 중심좌표를 리스트로 받는것
        # input_radius는 센서의 반지름을 입력받는거
        self.screen_size = (1360, 768)  # 손댈거없음
        self.polygon = [] + input_list  # 손댈거없음
        self.countpicture = 0  # 손댈거없음
        self.sensor = [] + input_sensor  # 손댈거없음
        self.sensor_radius = input_radius  # 손댈거없음

    def runGame(self, screen):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False

            pygame.draw.polygon(screen, (0, 0, 0),
                                self.polygon)  # 관심영역 그리기, screen에다가 (0,0,0)이니까 검정색으로, self.polygon이 관심영역의 꼭지점을 좌표로 받은거니이 꼭지점으로 다각형그리는거
            for number in self.sensor:  # 센서의 중심좌표 개수만큼 센서 그려주는거임
                pygame.draw.circle(screen, (180, 160, 100), number, self.sensor_radius, 0)
            pygame.display.update()  # 화면 업데이트
            pygame.image.save(screen, "image_test" + (str)(self.countpicture) + ".png")  # 상태저장
            self.countpicture = self.countpicture + 1
            run = False
        pygame.quit()

    def change_polygon(self, input_list):
        self.polygon.clear()
        self.polygon = input_list

    def change_radius(self, input_radius):
        self.sensor_radius = input_radius

    def save_png(self):  # 이 함수 호출하면 이제 죄다 실행되는거임
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size, DOUBLEBUF)
        screen.fill((255, 255, 255))  # 배경 흰색으로 채운거임
        #---------------------------------------------------------------이 위에는 이제 while문 위에 적히는 내용들 들어감
        self.runGame(screen)  # 본격적인 파이게임작동..(while문에 들어가야할 내용들)


#yeahgood = start(polygon_list, sensor_list, radius)  # 객체 생성
#yeahgood.its_main()  # 이거 호출하면이제 그냥 리스트대로 화면 캡처하고 저장해줌
#yeahgood.change_polygon(polygon_list2)  # 여기에다가 바꾼 리스트 넣으면 도형 바뀜
#yeahgood.change_radius(90)  # 센서 반지름 바꾸는 함수
#yeahgood.its_main()  # 바뀐고 보여줄려고 함수 호출한번 더함