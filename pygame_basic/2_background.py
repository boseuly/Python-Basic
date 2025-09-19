import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_heigth = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_heigth))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경이미지 불러오기
background = pygame.image.load("/Users/elena/PythonWorkspace/pygame_basic/background.jpg")


# 이벤트 루프 : 사용자가 마우스를 움직인다던가, 키보드를 사용한다던가의 동작을 계속 하고 있는지 확인하는 것
running = True # 게임이 진행 중인가 ?
while running: 
    for event in pygame.event.get(): # 이벤트가 발생했을 경우 처리를 해준다.
        if event.type == pygame.QUIT:  # 게임 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님


    # screen.fill((0,0,225)) # 이런 식으로 백그라운드 컬러를 채울 수도 있음
    screen.blit(background, (0, 0)) # blit을 통해서 배경 그리기
    pygame.display.update() # 게임 화면을 계속해서 그려주는 친구 !


# pygame 종료
pygame.quit()