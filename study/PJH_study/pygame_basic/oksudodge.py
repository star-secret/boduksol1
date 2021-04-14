import pygame

pygame.init() #초기화 과정


#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#pygame의 매소드 호출

#화면 타이틀 설정
pygame.display.set_caption("Oksudodge") #게임 이름

# FPS
clock = pygame.time.Clock()

#1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트)
       
#배경 설정
background = pygame.image.load("C:/Users/빡재형이/Desktop/PythonGame/pygame_basic/background.png")
#copy path, 탈출문자 처리
    
#캐릭터 불러오기
character = pygame.image.load("C:/Users/빡재형이/Desktop/PythonGame/pygame_basic/sunghun.png")
character_size = character.get_rect().size #이미지의 크기를 구해오기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width-character_width)/2 #화면 가로크기 절반에 해당하는 곳에 위치
character_y_pos = screen_height-character_height #화면 세로크기에 해당하는 곳에 위치

#캐릭터의 이동 위치
to_x = 0

running = True
while running :
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            
        if event.type == pygameKEYUP:
            if event.key == pygame.k_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
             
    character_x_pos += to_x

    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
         character_x_pos = screen_width - character_width
        
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))

