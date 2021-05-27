import pygame,sys

pygame.init()      #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480   #가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game")

# 배경 이미지 불러오기
background = pygame.image.load("background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size      #이미지의 크기를 [가로,세로]형태로 받아옴
character_width = character_size[0]             #캐릭터의 가로 크기
character_height = character_size[1]             #캐릭터의 세로 크기
character_x_pos = (screen_width-character_width) /2       # 화면 가로 크기의 절반 크기에 해당하는 곳에 캐릭터의 x값이 위치
character_y_pos = screen_height - character_height         # 화면 세로 크기의 가장 아래에 캐릭터의 y값이 위치

#이벤트 루프 - 사용자가 키를 입력하거나 마우스를 움직이거나 하는
#동작을 계속 감지하는 이벤트 루프가 있음
#파이 게임에서는 이 이벤트루프가 계속 실행되고 있어야 창이 꺼지지 않음

running = True  #게임이 진행중인지 확인
while running:
    for event in pygame.event.get():    #이벤트(마우스,키보드) 체크
        if event.type == pygame.QUIT:    #일반적인 창에 있는 x버튼을 눌렀을 때 발생하는 이벤트
            running = False     #게임 진행 중 아님
    
    screen.blit(background, (0,0))  #배경 그리기

    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update() #게임화면 다시 그리기 (파이게임에서는 매 프레임마다 화면을 다시 그려줘야함)
# pygame 종료
pygame.quit()
sys.exit()

