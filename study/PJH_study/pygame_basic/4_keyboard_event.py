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

#캐릭터 불러오기
character = pygame.image.load("C:/Users/빡재형이/Desktop/PythonGame/pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해오기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width-character_width)/2 #화면 가로크기 절반에 해당하는 곳에 위치
character_y_pos = screen_height-character_height #화면 세로크기에 해당하는 곳에 위치

#이동할 좌표
to_x = 0
to_y = 0



#이벤트 루프
running = True #게임이 진행중이라면
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하면
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -=5
            elif event.key == pygame.K_RIGHT:
                to_x +=5
            elif event.key == pygame.K_DOWN:
                to_y +=5
            elif event.key == pygame.K_UP:
                to_y -=5
        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 #더이상 움직이지 말라는 것
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0 #더이상 움직이지 말라는 것'

    character_x_pos += to_x
    character_y_pos += to_y

    #화면 밖으로 나가는거 방지
    if character_x_pos < 0:
        character_x_pos =0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    if character_y_pos < 0:
        character_y_pos =0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    screen.blit(background, (0,0))
     #배경의 위치를 튜플로 설정
    screen.blit(character,(character_x_pos, character_y_pos))

    pygame.display.update() 
    #게임화면 다시 그리기

#pygame 종료
pygame.quit()