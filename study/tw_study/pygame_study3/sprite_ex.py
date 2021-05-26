import math, sys
import pygame
from pygame.locals import *
 
pygame.init()
screen = pygame.display.set_mode((1024, 768), DOUBLEBUF)
clock = pygame.time.Clock()
 
class SimpleSprite(pygame.sprite.Sprite):       #sprtie클래스를 상속받는 새로운 클래스 sinplesprite를 정의한다
                                                #이 클래스를 정의하는 이유는 이 클래스를 이용해서 드론 객체를 생성할 것이기 때문
    def __init__(self, image, position):        #클래스 생성자, simpleSprite 클래스를 이용해서 객체를 생성할 때,이미지와
        pygame.sprite.Sprite.__init__(self)     #그 이미지가 위치할 좌표를 같이 받아야 한다.
        self.user_src_image = pygame.image.load(image)  # -> 인자로 들오온 것의 이미지를 받아옴
        self.user_position = position                   # -> 인자로 들어온 것의 위치를 받아옴
        self.user_rotation = 0                         # -> 처음 얼마나 회전해 있을지를 설정해줌. 지금은 회전 없이 이미지 그대로 시작
        self.user_speed = 0
        self.user_rotation_speed = 0
 
    def update(self, deltat):
        # 속도, 회전 속도에 따라 위치 정보를 업데이트한다   이미지가 바뀌면 상태를 업데이트하는 것
        self.user_rotation += self.user_rotation_speed      #이 코드는 이미지를 user_rotation_speed만큼 회전시킬 수 있다는 것
        x, y = self.user_position                           # 기존의 x,y좌표를 넣어줌
        rad = self.user_rotation * math.pi / 180            # pygame에서 각도는 rad을 이용함. 우리에게 익숙한 180분법을 이용하기 위한 코드
        x += -self.user_speed * math.sin(rad)               # x의 좌표를 업데이트
        y += -self.user_speed * math.cos(rad)               # y의 좌표를 업데이트
        self.user_position = (x, y)                         # 바뀐 x,y의 좌표를 객체의 x,y좌표로 집어 넣음
 
        self.image = pygame.transform.rotate(self.user_src_image, self.user_rotation)   #기존 이미지를 회전시킨 이미지로 변경
        self.rect = self.image.get_rect()                                               #회전시킨 이미지의 rect정보를 불러와서 갱신
        self.rect.center = self.user_position                                           #현재위치가 rect의 중심이 되게 설정
        #기본적으로 이미지는 화면에 그려지는 것으로, x,y좌표를 가지고 있지 않다. 이미지가 x,y좌표를 가질 수 있게 하려면 rect정보가 필요
 
class antidronesprite(pygame.sprite.Sprite):            #위와 비슷한 방식으로 드론이 아닌 핵심시설, antidrones을 표현할 클래스를   
                                                        #sprite클래스를 상속받아서 하나 더 작성
 
    def __init__(self, position):                       #우선 antidrones시스템들을 다 같은 도형으로 만들것이라서 위치만 받아옴
        pygame.sprite.Sprite.__init__(self)
        self.user_image_normal = pygame.image.load("triangl2.png")  #Antidrones시스템들을 어떤 도형으로 할지 도형을 받아옴
        self.user_image_hit = pygame.image.load("triangl2.png")
        self.user_position = position                               #만들어진 객체의 위치를 설정해줌
 
        self.image = self.user_image_normal                         
        self.rect = self.image.get_rect()                           #만들어진 객체의 rect정보를 받아옴
        self.rect.center = self.user_position                       #rect의 중심위치를 현재 객체의 위치로 설정
 
    def update(self, hit_list):
        
        if self in hit_list:
            self.image = self.user_image_hit
        else:
            self.image = self.user_image_normal
 
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position
 
rect = screen.get_rect()    #스크린의 rect정보를 받아옴
simple = SimpleSprite('triangl2.png', rect.center)  #simple이라는 객체를 SimpleSprite클래스를 이용해서 생성할 것
                                                    #여기서 simple객체는 드론을 의미함
                                                    #rect.center을 받았으므로 화면의 중심에 드론이 위치할 예정

simple_group = pygame.sprite.RenderPlain(simple)    #simple객체를 그룹화
                                    #나중에 여러 드론이 있을 상황을 가정하여 지금 하나의 드론이지만 그룹화를 통해서 코드를 작성

simple.mask = pygame.mask.from_surface(simple.user_src_image) 
                                    #sprite클래스에 있는 pygame.mask함수를 이용
                                    #이 함수는 이미지 그 자체를 인식할 수 있다
                                    #다른 것들은 이미지를 사각형의 형태, 원의 형태로만 인식할 수 있지만
                                    #mask를 설정하면 어떤 모양이든지 이미지를 그 자체로 인식할 수 있다.

blocks = [                          #Antidrones시스템들을 리스트로 선언함          
    antidronesprite((300, 400)),    #antidronesprite클래스를 이용하여서 객체를 생성하였음
    antidronesprite((800, 200)),
    antidronesprite((200, 600)),
    antidronesprite((800, 600))
]           
        #각각의 객체마다 mask를 설정 -> 이미지 그 자체를 인식할 수 있게끔 만들어 줌
blocks[0].mask = pygame.mask.from_surface(blocks[0].user_image_normal)
blocks[1].mask = pygame.mask.from_surface(blocks[1].user_image_normal)
blocks[2].mask = pygame.mask.from_surface(blocks[2].user_image_normal)
blocks[3].mask = pygame.mask.from_surface(blocks[3].user_image_normal)
block_group = pygame.sprite.RenderPlain(*blocks)    #여러 객체를 그룹화하여 한번에 다루기 쉽도록 설정
 
background = pygame.image.load('background1024768.png')
screen.blit(background, (0,0))
 
fontObj = pygame.font.Font(None, 32)       #폰트를 설정. None이므로 글꼴은 없고, 글자의 크기는 32
counter = 0 
while True:
    deltat = clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 

        # 키입력에 따라 속도, 회전 속도를 설정  드론을 직접 조종할 수 있게 키 입력에 따라 드론이 움직이게 설정.
        if hasattr(event, 'key'):
            down = event.type == KEYDOWN
            if event.key == K_RIGHT:
                simple.user_rotation_speed = down * -5 # 시계 방향이 마이너스인 것에 유의
                                                       # 키를 누르고 있는 동안 회전이 지속된다.
            elif event.key == K_LEFT:
                simple.user_rotation_speed = down * 5
            elif event.key == K_UP:                    # 키를 누르고 있으면 움직인다
                simple.user_speed = down * 4
            elif event.key == K_DOWN:
                simple.user_speed = down * -4

    counter += 1/deltat         #충돌할 때 까지 얼마의 시간이 걸렸는지 확인하기 위해 카운터를 설정
                                #deltat값은 프레임 값과 같은데 1초에 counter값이 1씩 올라가야함
                                #만약 프레임이 30이라면 counter += 1로 설정한다면 1초에 counter가 30씩 증가할 것임
                                #이것을 막기 위해 프레임값인 deltat로 나누어 줌
    simple_group.update(deltat) #매 프레임마다 드론의 상태를 업데이트
    
                      #mask충돌을 이용해서 이미지와 이미지가 겹칠때 충돌이라는 글자와 시작하고 얼마나 흘렀는지 콘솔창에 출력
    if(pygame.sprite.collide_mask(blocks[2],simple)): 
        print("충돌")
        print("count is{}".format(counter))
    if(pygame.sprite.collide_mask(blocks[1],simple)):
        print("충돌")
        print("count is{}".format(counter))
    if(pygame.sprite.collide_mask(blocks[0],simple)):
        print("충돌")
        print("count is{}".format(counter))
    if(pygame.sprite.collide_mask(blocks[3],simple)):
        print("충돌")
        print("count is{}".format(counter))
    #도형이 움직이면 잔상이 남는데 그 잔상을 지워주기 위해 clear를 한 다음에 다시 그린다.
    simple_group.clear(screen, background)
    block_group.clear(screen, background)
    simple_group.draw(screen)
    block_group.draw(screen)
    pygame.display.update()

