import pygame
# @@@@ 기본 뼈대로 해당 파일 사용하기 @@@@  #
############################ 기본 초기화 (반드시 해야 하는 것들) ##########################

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_heigth = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_heigth))

# 화면 타이틀 설정
pygame.display.set_caption("피해랏") # 게임 이름

# FPS
clock = pygame.time.Clock()
#####################################################################################

############## 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트, 등 ##################



#################################### 이벤트 루프 #######################################

# 이벤트 루프 : 사용자가 마우스를 움직인다던가, 키보드를 사용한다던가의 동작을 계속 하고 있는지 확인하는 것
running = True # 게임이 진행 중인가 ?
while running: 
    dt = clock.tick(40) 

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): # 이벤트가 발생했을 경우 처리를 해준다.
        if event.type == pygame.QUIT:  # 게임 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리
    
        
    # 5. 화면에 그리기
    
    pygame.display.update() # 게임 화면을 계속해서 그려주는 친구 !

# pygame 종료
pygame.quit()

