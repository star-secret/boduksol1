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

# FPS
clock = pygame.time.Clock()
       
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

# 적 캐릭터 설정
enemy = pygame.image.load("C:/Users/빡재형이/Desktop/PythonGame/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해오기
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width-enemy_width)/2 #화면 가로크기 절반에 해당하는 곳에 위치
enemy_y_pos = (screen_height/2)-(enemy_height/2) #화면 세로크기에 해당하는 곳에 위치

#이동할 좌표
to_x = 0
to_y = 0

#이동속도
character_speed =0.6


#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체를 생성하고 디폴트값을 넣고 크기를 설정한다

#총 시간
total_time = 10

#시작 시간 정보
start_ticks = pygame.time.get_ticks() #시간 tick을 받아줌

#이벤트 루프
running = True #게임이 진행중이라면
while running:
    dt = clock.tick(30) #게임화면의 초당 프레임 수를 변경

#캐릭터가 100만큼 이동해야 한다면
#10 fps : 1초 동안 10번 동작 10만큼
#20 fps : 1초 동안 20번 동작 5만큼

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하면
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x +=character_speed
            elif event.key == pygame.K_DOWN:
                to_y +=character_speed
            elif event.key == pygame.K_UP:
                to_y -=character_speed
        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 #더이상 움직이지 말라는 것
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0 #더이상 움직이지 말라는 것'

    character_x_pos += to_x *dt
    character_y_pos += to_y *dt

    #화면 밖으로 나가는거 방지
    if character_x_pos < 0:
        character_x_pos =0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos =0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    #충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top=enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어")
        running = False

    screen.blit(background, (0,0))
     #배경의 위치를 튜플로 설정
    screen.blit(character,(character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    #주인공과 적 캐릭터 위치
   

    #타이머 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks()-start_ticks)/1000 #경과시간을 1000으로 나누어서 초단위로 표시

    timer = game_font.render(str(int(total_time-elapsed_time)), True, (255, 255, 255))
    #시간 정보, True, 글자색상
    screen.blit(timer, (10,10))
    if total_time - elapsed_time <=0:
        print("타임오버")
        running = False
    
    pygame.display.update() 
    #게임화면 다시 그리기
#잠시대기
Pygame.time.delay(2000) #2초간 대기
#pygame 종료
pygame.quit()