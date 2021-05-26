import math, sys
import pygame
import time, random
from pygame.locals import *
####
# 
# 
#  
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
        
        if self in hit_list:
            self.image = self.user_image_hit
        else:
            self.image = self.user_image_normal
 
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
antidrones = [
    AntidroneSprite((adx[0], ady[0])),
    AntidroneSprite((adx[1], ady[1])),
    AntidroneSprite((adx[2], ady[2])),
    AntidroneSprite((adx[3], ady[3])),
]
c=100000
go_x=0
go_y=0
for i in range(0,3,1):
    a = adx[i] - bd_x
    b = ady[i] - bd_y
    d = math.sqrt((a*a)+(b*b))
    if(c>d):
        c=d
        go_x=a
        go_y=b


antidrones[0].mask = pygame.mask.from_surface(antidrones[0].user_image_normal)
antidrones[1].mask = pygame.mask.from_surface(antidrones[1].user_image_normal)
antidrones[2].mask = pygame.mask.from_surface(antidrones[2].user_image_normal)
antidrones[3].mask = pygame.mask.from_surface(antidrones[3].user_image_normal)
block_group = pygame.sprite.RenderPlain(*antidrones)
 
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
        
        drone.user_yspeed = -go_y/100
        drone.user_xspeed = -go_x/100
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
    
   # collisions = pygame.sprite.spritecollide(drone, block_group, False)
    if(pygame.sprite.collide_mask(antidrones[2],drone) and startflag==0):
        print("충돌")
        counter = 0
        startflag = 1
        time.sleep(3)
        
    if(pygame.sprite.collide_mask(antidrones[1],drone) and startflag==0):
        print("충돌")
        counter = 0
        startflag = 1
        time.sleep(3)
    if(pygame.sprite.collide_mask(antidrones[0],drone) and startflag==0):
        print("충돌")
        counter = 0
        startflag = 1
        time.sleep(3)
    if(pygame.sprite.collide_mask(antidrones[3],drone) and startflag==0):
        print("충돌")
        counter = 0
        startflag = 1
        time.sleep(3)

        
    pygame.draw.polygon(screen,(0,0,0),polygon_list,5)   
    drone_group.clear(screen, background)
    block_group.clear(screen, background)
    drone_group.draw(screen)
    block_group.draw(screen)
    screen.blit(textSurfaceObj,(50,50))
    pygame.display.update()

