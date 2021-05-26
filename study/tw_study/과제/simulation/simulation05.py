import math, sys
import pygame
import time, random
from pygame.locals import *

#### 드론 속도조절

pygame.init()
screen_size= (1360,768)
screen = pygame.display.set_mode(screen_size, DOUBLEBUF)
clock = pygame.time.Clock()

startflag=0

class droneSprite(pygame.sprite.Sprite):
 
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.user_src_image = pygame.image.load(image)
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
 
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.user_image_normal = pygame.image.load("triangl2.png")
        self.user_image_hit = pygame.image.load("triangl2.png")
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
        self.user_image_normal = pygame.image.load("hackseemshesoul.png")
        self.user_image_hit = pygame.image.load("hackseemshesoul.png")
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
bd_x =random.randrange(0,480)                       # 드론 x 좌표 랜덤
bd_y =random.randrange(0,640)                       # 드론 y좌표 랜덤
drone = droneSprite('blackdrone.png', (bd_x,bd_y)) # 드론 생성

drone_group = pygame.sprite.RenderPlain(drone)
drone.mask = pygame.mask.from_surface(drone.user_src_image) 

adx = [300,800,200,800]
ady = [400,20,600,600]
#안티드론 만들기
antidrones = []
for i in range(0,len(adx),1):
    antidrones.append(AntidroneSprite((adx[i], ady[i])))

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
 
fontObj = pygame.font.Font(None, 32)

counter = 0 

#관심영역 만들기
polygon_list = []
polygon_list.append([30,0])
polygon_list.append([1000,700])
polygon_list.append([30,500])



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
        
        drone.user_yspeed = -go_y*2/deltat
        drone.user_xspeed = -go_x*2/deltat
        # 키입력에 따라 속도, 회전 속도를 설정
        if hasattr(event, 'key'):
            down = event.type == KEYDOWN
            if event.key == K_RIGHT:
                drone.user_rotation_speed = down * -5 # 시계 방향이 마이너스인 것에 유의
            elif event.key == K_LEFT:
                drone.user_rotation_speed = down * 5
            elif event.key == K_UP:
                drone.user_yspeed = down * 4
            elif event.key == K_DOWN:
                drone.user_yspeed = down * -4
            elif event.key == K_SPACE:
                time.sleep(3)
                counter = 0
                

    counter += 1/deltat
    drone_group.update(deltat)
    hackseem_group.update(deltat)


    for i in range (0,len(antidrones),1):
        if(pygame.sprite.collide_mask(antidrones[i],drone) and startflag==0):
            print("충돌")
            counter = 0
            startflag = 1

    for i in range (0,len(hackseems),1):
        if(pygame.sprite.collide_mask(hackseems[i],drone) and startflag==1):
            print("테러진행")
            time.sleep(3)
        
    pygame.draw.polygon(screen,(0,0,0),polygon_list,5)   
    drone_group.clear(screen, background)
    hackseem_group.clear(screen, background)
    antidrone_group.clear(screen, background)
    hackseem_group.draw(screen)
    drone_group.draw(screen)
    antidrone_group.draw(screen)
    screen.blit(textSurfaceObj,(50,50))
    pygame.display.update()

