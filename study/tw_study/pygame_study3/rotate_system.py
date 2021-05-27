import math,sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1024,768))
clock = pygame.time.Clock()

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
simple = RotateSprite("triangl2.png",rect.center)
simple_group = pygame.sprite.RenderPlain(simple)    #RenderPlain : 여러개의 스프라이트를 묶어주는 역할

background = pygame.image.load("background1024768.png")
screen.blit(background,(0,0))

while(True):
    deltat = clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    simple_group.update(deltat)     #상태업데이트 (즉 회전이 계속 이루어진다는 것을 업데이트)
    simple_group.clear(screen,background)
    simple_group.draw(screen)       # Renderplain객체를 통해 출력할 때
    pygame.display.flip()