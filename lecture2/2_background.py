import pygame
pygame.init()           # 초기화 (반드시 필요, 실행 시 필수입력)

# 화면크기 설정
screen_width = 480      # 가로 크기
screen_height = 640     # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")      # 게임이름 입력

# 배경 이미지 불러오기
background = pygame.image.load("C:/python/python-practice/lecture2/background.png")

# 이벤트 루프
running = True          # 게임이 진행중인가?
while running:
   for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
      if event.type == pygame.QUIT:    # 창이 닫히는 이벤트가 발생하였는가?
         running = False               # 게임이 진행중이 아니다.

   #screen.fill((0, 0, 225))           # 입력된 (R,G,B) 비율에 따라 화면을 채웁니다.
   screen.blit(background, (0, 0))     # (게임이 진행중인 동안) background이미지를 (0,0) 좌표에서 실행시킵니다)  # 배경그리기
                                       # 좌측 상단을 기준으로 좌표를 계산 (좌측최상단 = 0,0)
   pygame.display.update()             # 게임화면을 다시 그리기 (미호출시 반영이 되지 않음)
# pygame 종료
pygame.quit()