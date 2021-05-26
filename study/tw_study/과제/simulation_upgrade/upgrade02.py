import math, sys
import pygame
import time, random
from pygame.locals import *

####05 드론 속도조절
####06 드론 크기변경&센서 크기 입력 받기 & 타이머 수정(충돌시 0에서 흘러가게)

pygame.init()
screen_size= (1360,768)
screen = pygame.display.set_mode(screen_size, DOUBLEBUF)
clock = pygame.time.Clock()
pygame.display.set_caption("Anti drones 시스템의 배치 최적화")
startflag=0

class droneSprite(pygame.sprite.Sprite):
 
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.user_src_image = pygame.transform.scale(pygame.image.load(image),(5,5))
        self.user_position = position
        self.user_rotation = 0
        self.user_xspeed = 0
        self.user_yspeed = 0
        self.user_rotation_speed = 0
 
    def update(self, deltat):
        # 속도, 회전 속도에 따라 위치 정보를 업데이트한다
        self.user_rotation += self.user_rotation_speed
        x, y = self.user_position
        rad = self.user_rotation * math.pi / 180
        x += -self.user_xspeed
        y += -self.user_yspeed
        self.user_position = (x, y)
 
        self.image = pygame.transform.rotate(self.user_src_image, self.user_rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position
 
class AntidroneSprite(pygame.sprite.Sprite):
 
    def __init__(self, position,rad):
        pygame.sprite.Sprite.__init__(self)
        self.user_image_normal = pygame.transform.scale(pygame.image.load("antidrone_circle2.png"),(2*rad,2*rad))
        self.user_position = position
 
        self.image = self.user_image_normal
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position
 
    def update(self, hit_list):
        

        self.rect = self.image.get_rect()
        self.rect.center = self.user_position

class hackseemSprite(pygame.sprite.Sprite):
 
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.user_image_normal = pygame.image.load("haackseemshesoul2.png")
        self.user_position = position
 
        self.image = self.user_image_normal
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position
 
    def update(self, hit_list):
 
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position

class RotateSprite(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.user_src_image = pygame.image.load(image)
        self.user_position = position
        self.user_rotation = 20
        self.user_speed = 0
        self.user_rotation_speed = 5        #+는 반시계 방향, 시계방향으로 돌리려면 -해야함
    
    def update(self, deltat):
        self.user_rotation += self.user_rotation_speed
        x,y = self.user_position
        rad = self.user_rotation *math.pi
        x += -self.user_speed * math.sin(rad)
        y += -self.user_speed * math.cos(rad)
        self.user_position = (x,y)

        self.image = pygame.transform.rotate(self.user_src_image, self.user_rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position



rect = screen.get_rect()
bd_x =random.randrange(0,1200)                       # 드론 x 좌표 랜덤
bd_y =random.randrange(0,640)                       # 드론 y좌표 랜덤
drone = droneSprite('blackdrone.png', (bd_x,bd_y)) # 드론 생성

bd_xs =[]#

bd_ys=[]

drones=[]#
for i in range(0,17,1):#
    bd_xs.append(70*(i+1))
    bd_ys.append(100)
    drones.append(droneSprite('blackdrone.png',(bd_xs[i],bd_ys[i])))#
for i in range(17,17+17,1):#
    bd_xs.append(70*(i-16))
    bd_ys.append(700)
    drones.append(droneSprite('blackdrone.png',(bd_xs[i],bd_ys[i])))#
for i in range(17+17,17+17+12,1):
    bd_xs.append(70)
    bd_ys.append(50+(i-34)*50)
    drones.append(droneSprite('blackdrone.png',(bd_xs[i],bd_ys[i])))#
for i in range(17+17+12,17+17+12+12,1):
    bd_xs.append(1300)
    bd_ys.append(50+(i-34-12)*50)
    drones.append(droneSprite('blackdrone.png',(bd_xs[i],bd_ys[i])))#
drone_group = pygame.sprite.RenderPlain(drone,drones)#

drone.mask = pygame.mask.from_surface(drone.user_src_image) 

for i in range(0,10,1):#
    drones[i].mask=pygame.mask.from_surface(drones[i].user_src_image) 

adx = [300,200,800,100,460,320,490,650]
ady = [400,600,600,125,265,654,420,380]
#안티드론 만들기
antidrones = []
for i in range(0,len(adx),1):
    antidrones.append(AntidroneSprite((adx[i], ady[i]),100))

hackx=[300,700]
hacky=[470,400]
hackseems = []
for i in range(0,len(hackx),1):
    hackseems.append(hackseemSprite((hackx[i],hacky[i])))

c=100000
go_x=0
go_y=0
for i in range(0,len(hackseems),1):
    a = hackx[i] - bd_x
    b = hacky[i] - bd_y
    d = math.sqrt((a*a)+(b*b))
    if(c>d):
        c=d
        go_x=a/c
        go_y=b/c
########################
go_xs=[]
go_ys=[]
for i in range(0,len(drones),1):
    c=100000
    go_xs.append(0)
    go_ys.append(0)
    for j in range(0,len(hackseems),1):
        a = hackx[j] - bd_xs[i]
        b = hacky[j] - bd_ys[i]
        d = math.sqrt((a*a)+(b*b))
        if(c>d):
            c=d
            go_xs[i]=(a/c)
            go_ys[i]=(b/c)
#########################

#안티드론 그룹
for i in range(0,len(antidrones),1):
    antidrones[i].mask = pygame.mask.from_surface(antidrones[i].user_image_normal)
antidrone_group = pygame.sprite.RenderPlain(*antidrones)

#핵심시설 그룹
for i in range(0,len(hackseems),1):
    hackseems[i].mask = pygame.mask.from_surface(hackseems[i].user_image_normal)
hackseem_group = pygame.sprite.RenderPlain(*hackseems)

background = pygame.image.load('background1360768.png')
screen.blit(background, (0,0))

#시간폰트 
fontObj = pygame.font.Font(None, 32)
#테러폰트
fontTerror = pygame.font.Font(None,25)

counter = 0 

#관심영역 만들기
polygon_list = []
polygon_list.append([10,10])
polygon_list.append([1200,10])
polygon_list.append([1200,700])
polygon_list.append([10,700])

timer_start = 0
time.sleep(2)
index=0
while True:
    
    deltat = clock.tick(30)
    textSurfaceObj = fontObj.render("count is{}".format(counter), True, (255,0,10))   
    textRectObj = textSurfaceObj.get_rect()         #텍스트 객체의 출력 위치를 가져오기 위함
    textRectObj.center = (50,50)
    subsurface_rect = pygame.Rect(50,50,400,60)
    subsrface= screen.subsurface(subsurface_rect)
    subsrface.fill((181,230,29))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #드론속도

    drone.user_yspeed = -go_y*3/2#*4/deltat
    drone.user_xspeed = -go_x*3/2#*4/deltat

        #####
    for i in range(0,len(drones),1):
        drones[i].user_yspeed = -go_ys[i]/2
        drones[i].user_xspeed = -go_xs[i]/2


    if (timer_start == 1):
        counter += 1/deltat
    drone_group.update(deltat)
    hackseem_group.update(deltat)

    
    for i in range (0,len(antidrones),1):
        if(pygame.sprite.collide_mask(antidrones[i],drone) and startflag==0):
            print("충돌")
            timer_start = 1
            counter = 0
            startflag = 1
            index=i

    for i in range (0,len(hackseems),1):
        if(pygame.sprite.collide_mask(hackseems[i],drone) and startflag==1):

            print("테러진행")
            time.sleep(3)
            drone.user_position=(bd_x,bd_y)
            adx[index]=adx[index]-go_x*30
            ady[index]=ady[index]-go_y*30
            antidrones[index].user_position=(adx[index],ady[index])
            antidrones[index].rect.center=(adx[index],ady[index])
            startflag=0
        
    pygame.draw.polygon(screen,(255,255,255),polygon_list,5)   
    drone_group.clear(screen, background)
    hackseem_group.clear(screen, background)
    antidrone_group.clear(screen, background)
    hackseem_group.draw(screen)

    antidrone_group.draw(screen)
    screen.blit(textSurfaceObj,(50,50))
    drone_group.draw(screen)  

    pygame.display.update()

