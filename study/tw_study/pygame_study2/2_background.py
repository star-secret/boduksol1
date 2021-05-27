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

#이벤트 루프 - 사용자가 키를 입력하거나 마우스를 움직이거나 하는
#동작을 계속 감지하는 이벤트 루프가 있음
#파이 게임에서는 이 이벤트루프가 계속 실행되고 있어야 창이 꺼지지 않음

running = True  #게임이 진행중인지 확인
while running:
    for event in pygame.event.get():    #이벤트(마우스,키보드) 체크
        if event.type == pygame.QUIT:    #일반적인 창에 있는 x버튼을 눌렀을 때 발생하는 이벤트
            running = False     #게임 진행 중 아님
    screen.blit(background, (0,0))  #배경 그리기
#   screen.fill((0,0,255))  만약 배경을 load로 불러오지 않는다면, 이렇게 fill()메소드를 이용하여서 배경색을 전부 채울 수도 있다

    pygame.display.update() #게임화면 다시 그리기 (파이게임에서는 매 프레임마다 화면을 다시 그려줘야함)
# pygame 종료
pygame.quit()
sys.exit()

