import sys,pygame,math
from pygame.locals import *

pygame.init()
size=(1024,768)
screen = pygame.display.set_mode(size)
#FPS
clock = pygame.time.Clock()
#FONT
fontObj = pygame.font.Font(None, 32)
#카운트
counter = 0
#회전할 이미지
triangle = pygame.image.load("triangl2.png")    #반환값 : surface객체를 반환
theta = 0

running = True  
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    ''' 시간 재는 부분'''
    counter +=(1/60)
    screen.fill((0,0,0))
    count_image = fontObj.render("count is{}".format(counter), True, (225,225,225))
    screen.blit(count_image,(50,50))
    '''시간 재는 부분 끝 '''
    
    '''회전시키기'''
    theta += math.radians(180)/dt          #1도씩 회전
    new_triangle = pygame.transform.rotate(triangle, theta)
    rect = new_triangle.get_rect()  #이미지가 차지하는 직사각형을 get_rect()로 구함
    rect.center = (200,150)         #중심설정 이 중심기준으로 회전
    screen.blit(new_triangle,(rect))
    '''회전시키기 끝'''
    pygame.display.update()
   
        