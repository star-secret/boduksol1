import pygame,sys

pygame.init()      


screen_width = 480  
screen_height = 640 
screen = pygame.display.set_mode((screen_width,screen_height))

clock = pygame.time.Clock()
pygame.display.set_caption("Game")

#화면에 글자 띄우기
#폰트설정
fontObj = pygame.font.Font(None, 32)    #None = 글꼴을 설정하지 않음, 기본폰트, 텍스트 크기는 32
#텍스트가 표시된 surface를 만듬
textSurfaceObj = fontObj.render('font', True, (0,240,10))   # 첫번째 인자는 출력 내용,두번째는 Anti-aliasing사용 여부,세번째는 색
#텍스트 표시될 위치 설정
textRectObj = textSurfaceObj.get_rect()         #텍스트 객체의 출력 위치를 가져오기 위함
textRectObj.center = (150,150)                  #텍스트 객체의 출력 중심의 좌표
#텍스트를 화면에 표시
screen.blit(textSurfaceObj, textRectObj) 



running = True  
while running:
    clock.tick(20)
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:   
            running = False  
  
    pygame.display.update()

# pygame 종료
pygame.quit()
sys.exit()
