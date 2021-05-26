import pygame,sys
class Block(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = img
        self.rect = img.get_rect()


pygame.init()      #초기화 (반드시 필요)


screen_width = 480  
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("마우스 따라 움직이는 드론")

drone_pic = pygame.image.load("cccc.png").convert_alpha()   #드론 이미지 생성
drone_pic = pygame.transform.scale(drone_pic,(30,30))       #드론 이미지의 크기를변경

drone = Block(drone_pic)
drone.rect.center=(410,700)


running = True  #게임이 진행중인지 확인
while running:
    for event in pygame.event.get():    #이벤트(마우스,키보드) 체크
        if event.type == pygame.QUIT:    #일반적인 창에 있는 x버튼을 눌렀을 때 발생하는 이벤트
            running = False     #게임 진행 중 아님
        if event.type == pygame.MOUSEMOTION: #마우스를 움직였을 때
            drone.rect.center = (pygame.mouse.get_pos())
    pygame.display.flip()
# pygame 종료
pygame.quit()
sys.exit()
