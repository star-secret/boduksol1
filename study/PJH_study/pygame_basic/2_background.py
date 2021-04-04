import pygame


pygame.init() #초기화 과정


#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
pygame.display.set_mode((screen_width, screen_height))

screen = pygame.display.set_mode((480, 640))
#pygame의 매소드 호출

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

       
#배경 설정
background = pygame.image.load("C:/Users/빡재형이/Desktop/PythonGame/pygame_basic/background.png")
#copy path, 탈출문자 처리


#이벤트 루프
running = True #게임이 진행중이라면
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하면
            running = False


    screen.fill((0,0,225))
    # screen.blit(background, (0,0))
     #배경의 위치를 튜플로 설정
    pygame.display.update() 
    #게임화면 다시 그리기

#pygame 종료
pygame.quit()

