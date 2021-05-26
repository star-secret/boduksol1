import math, sys
import pygame
import time, random
from pygame.locals import *


pygame.init()   #이것은 pygame초기화하는거라서 앞에 무조건 있어야함 


screen_size= (1360,768)     #이거는 실행시 화면 사이즈를 얼마로 할지 내가 정해준거 가로1360픽셀 세로 768픽셀
                            #화면을 만든게 아니라 화면 사이즈만 설정해준거

screen = pygame.display.set_mode(screen_size, DOUBLEBUF)    #화면을 만드는거임. screen_size에는 화면 사이즈, DOUBLEBUF는 그냥 모드


clock = pygame.time.Clock()             #이거는 시간 체크할려고 시간 객체만드는거

pygame.display.set_caption("Anti drones 시스템의 배치 최적화")  #이거는 화면 타이틀창? 화면의 이름 정해주는거


#여기서부터는 sprite class를 상속받아서 내가 새로운 class를 정의하는 거임
#drone을 생성할때 사용함.
class droneSprite(pygame.sprite.Sprite):
 
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)

        self.user_src_image = pygame.transform.scale(pygame.image.load(image),(20,20))  
            #이거는 이미지크기를 transform.scale로 조정하는가임. 뒤에 (20,20)의미는 가로 20 세로 20의 사각형안에 이 그림이 있다는 것을 의미
          
        self.user_position = position
                #위치 설정
                     
        self.user_rotation = 0
                #이게 0이면 그림 그대로 나옴. 만약에 숫자 들어가면 회전된 상태에서 나옴

        self.user_xspeed = 0
                # 초기 x방향 스피드 (0으로 설정되어 있으니 안움직임)
        self.user_yspeed = 0
                # 초기 y방향 스피드 (0으로 설정되어 있으니 안움직임)
        self.user_rotation_speed = 0
                # 초기 회전속도. 이게 0이아니면 회전함
 
    def update(self, deltat):
        # 속도, 회전 속도에 따라 위치 정보를 업데이트한다
        self.user_rotation += self.user_rotation_speed      #회전속도가 주어지면 rotation을 계속 더해줌. 그럼 계속 회전하겠지

        x, y = self.user_position              #위치랑 관련된거. 잘 모르지만 있어야함

        rad = self.user_rotation * math.pi / 180    #회전을 rad으로 설정해줄려고하는거

        x += -self.user_xspeed      #x축 방향으로 속도가 존재하면 그속도만큼 계속 x를 더해주어야 된다

        y += -self.user_yspeed

        self.user_position = (x, y)     #위치랑 관련된거. 잘 모르지만 있어야함
 
        self.image = pygame.transform.rotate(self.user_src_image, self.user_rotation)       #잘 모르지만 있어야함
                    
        self.rect = self.image.get_rect()       #그림에 있는 좌표랑 충돌처리를 위한 좌표를 일치시켜주는건데. 잘 모르지만 있어야함.
        self.rect.center = self.user_position
 




bd_xs =[]       #드론의 초기 x위치를 이 리스트에 담아줄거임
bd_ys=[]        # 드론의 초기 y위치를 이 리스트에 담아줄거임

drones=[]       # 드론들의 리스트

#드론의 x좌표랑 y좌표를 만들어주고 그 x,y에 해당하는 드론을 생성해서 drones 리스트에 넣어줌
for i in range(0,10,1):#
    bd_xs.append(70*(i+1))
    bd_ys.append(100)
    drones.append(droneSprite('blackdrone.png',(bd_xs[i],bd_ys[i])))#


drone_group = pygame.sprite.RenderPlain(drones)     #드론 그룹핑

#이건 충돌처리를 위한 mask 지정. 그러니까 이미지만을 딴다?라고 보면될듯.
for i in range(0,10,1):#
    drones[i].mask=pygame.mask.from_surface(drones[i].user_src_image) 

#뒤에 초록색으로 나오는 배경 객체를 만들어줌
background = pygame.image.load('background1360768.png')

#이 배경 객체를 screen에다가 나오게 해줌
screen.blit(background, (0,0))

#시간폰트 
fontObj = pygame.font.Font(None, 32)


#충돌까지 시간잴려고 만들어 논거긴함
counter = 0 

#관심영역 만들기
#코드 마지막에 보면     pygame.draw.polygon(screen,(255,255,255),polygon_list,5)   가 있음
#여기서 다각형 그릴려면 다각형의 꼭짓점을 리스트로 주어야함
#그래서 여기서 꼭짓점을 리스트로 받음
#근데 이때 추가하는 순서가 중요함, 왜냐하면 다각형을 그리는게 아니라 주어진 순서대로 꼭짓점으로해서 선을 긋는다?라고 보는게 맞기 때문
polygon_list = []
polygon_list.append([10,10])
polygon_list.append([1200,10])
polygon_list.append([1200,700])
polygon_list.append([10,700])


index=0     #드론의 index임. 버전마다 다른 드론 조종할 수 있게 할려고 만든거임

while True:
    
    deltat = clock.tick(30)     # clock.tick(30)은 화면을 1초에 30번깜박이게 하는건데 반환값이 뭔지 기억안남.. 근데 있어야함
                                #화면을 1초에 60번 빠르게 하면 이동속도가 빨라짐
                                #예를들면 x방향이동속도를 5라고 가정하면 1초에 30번깜박일때는 150픽셀이동, 1초에 60번이면 300픽셀 이동
                                #그래서 이 프레임이 바뀌어도 일정한 속도를 유지하게 하기 위해서 이동속도/deltat를 하면 1초당 깜박이는 수가 바뀌어도 같은 속도로 이동

    #시간 출력과 관련된 것들
    counter += 1/deltat
    textSurfaceObj = fontObj.render("count is{}".format(counter), True, (255,0,10))   #시간 출력! 뒤에 (255,0,10)은 색깔
    textRectObj = textSurfaceObj.get_rect()         #텍스트 객체의 출력 위치를 가져오기 위함
    textRectObj.center = (50,50)
    subsurface_rect = pygame.Rect(50,50,400,60)
    subsrface= screen.subsurface(subsurface_rect)
    subsrface.fill((181,230,29))
    #시간 출력은 위에 내용이 그대로 있어야함.

    #event시작
    for event in pygame.event.get():
        if event.type == QUIT:      #화면에 있는 x버튼 누르면 pygame 종료
            pygame.quit()
            sys.exit()

        
            
        
        #드론의 무우비잉을 표현
        if hasattr(event, 'key'):
            down = event.type == KEYDOWN
            if event.key == K_RIGHT:        #index에 해당하는 드론의 이동속도 조종
                drones[index].user_xspeed = down * -2 # 시계 방향이 마이너스인 것에 유의             
            elif event.key == K_LEFT:
                drones[index].user_xspeed = down * 2
            elif event.key == K_UP:
                drones[index].user_yspeed = down * 2
            elif event.key == K_DOWN:
                drones[index].user_yspeed = down * -2
            if event.key == K_a:        #a버튼 누르면 0번 드론
                index = 0
            if event.key == K_b:        #b버튼 누르면 1번드론
                index = 1
            if event.key == K_c:
                index = 2
            if event.key == K_d:
                index = 3
            if event.key == K_e:
                index = 4
            if event.key == K_f:
                index = 5
            if event.key == K_g:
                index = 6
            if event.key == K_h:
                index = 7
            if event.key == K_SPACE:
                pygame.image.save(screen,"image_test.png")      #이건 이제 스페이스바 누르면 현재의 화면을 캡처하는 거임
            if event.key == K_m:
                p,q = drones[index].user_position
                print("현재 드론 : " +(str)(index) + "x좌표 : " +(str)(p) + " y좌표 : "+(str)(q))
                






    drone_group.update(deltat)      #드론 그룹 업데이트. 그냥 있어야함

    
    
        
    pygame.draw.polygon(screen,(255,255,255),polygon_list,5)   #polygon 그리기
    drone_group.clear(screen, background)       #드론 잔상제거위해 clear하고 다시 draw해주어야함

    screen.blit(textSurfaceObj,(50,50))         #텍스트 화면에 출력
    drone_group.draw(screen)                    #드론그룹 그리기

    pygame.display.update()                     #화면 업데이트

