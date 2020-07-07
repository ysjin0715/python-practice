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

# 캐릭터(스프라이트) 블러오기
character = pygame.image.load("C:/python/python-practice/lecture2/character.png")
character_size = character.get_rect().size          # 이미지의 크기를 본파일에서 가져와 리스트화한다.
character_width = character_size[0]                 # 리스트화된 캐릭터의 크기정보 중 0번째를 가로크기로 정한다.
character_height = character_size[1]                # 리스트화된 캐릭터의 크기정보 중 1번째를 세로크기로 정한다.
character_x_pos = screen_width / 2-character_width / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치한다. (x좌표)
character_y_pos = screen_height-character_height    # 화면 세로크기 가장 아래에 해당하는 곳에 위치한다. (y좌표)

# 이벤트 루프
running = True          # 게임이 진행중인가?
while running:
   for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
      if event.type == pygame.QUIT:    # 창이 닫히는 이벤트가 발생하였는가?
         running = False               # 게임이 진행중이 아니다.

   screen.blit(background, (0, 0))     # (게임이 진행중인 동안) background이미지를 (0,0) 좌표에서 실행시킵니다)  # 배경그리기
                                       # 좌측 상단을 기준으로 좌표를 계산 (좌측최상단 = 0,0)
   screen.blit(character, (character_x_pos,character_y_pos))      # 캐릭터 그리기
   pygame.display.update()             # 게임화면을 다시 그리기 (미호출시 반영이 되지 않음)
# pygame 종료
pygame.quit()