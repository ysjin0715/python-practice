import pygame

pygame.init()  # 초기화 (반드시 필요, 실행 시 필수입력)

# 화면크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")  # 게임이름 입력

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/python/python-practice/lecture2/background.png")

# 캐릭터(스프라이트) 블러오기
character = pygame.image.load("C:/python/python-practice/lecture2/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 본파일에서 가져와 리스트화한다.
character_width = character_size[0]  # 리스트화된 캐릭터의 크기정보 중 0번째를 가로크기로 정한다.
character_height = character_size[1]  # 리스트화된 캐릭터의 크기정보 중 1번째를 세로크기로 정한다.
character_x_pos = screen_width / 2 - character_width / 2  # 화면 가로의 절반 크기에 해당하는 곳에 위치한다. (x좌표)
character_y_pos = screen_height - character_height  # 화면 세로크기 가장 아래에 해당하는 곳에 위치한다. (y좌표)

# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도
character_speed = 0.6

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
   dt = clock.tick(60)               # 게임화면의 초당 프레임수를 제한


#  캐릭터가 100만큼 이동을 해야한다 (프레임수에 따라서 캐릭터의 움직임이 달라진다)
# 10fps : 1초 동안 10번 동작 -> 10*10 = 100
# 20fps : 1초 동안 20번 동작 -> 5 *20 = 100

   print("fps : ",str(clock.get_fps()))
   for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
      if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
         running = False  # 게임이 진행중이 아니다.

      if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인한다.
         if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
            to_x -= character_speed
         elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
            to_x += character_speed
         elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
            to_y += character_speed
         elif event.key == pygame.K_UP:  # 캐릭터를 위로
            to_y -= character_speed

      if event.type == pygame.KEYUP:  # 방향키를 뗀다면
         if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0
         if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            to_y = 0

   character_x_pos += to_x * dt # x축 이동한 거리만큼 저장
   character_y_pos += to_y * dt # y축 이동한 거리만큼 저장

   # 가로 경계값 처리
   if character_x_pos < 0:
      character_x_pos = 0
   elif character_x_pos > screen_width - character_width:
      character_x_pos = screen_width - character_width

   # 세로 경계값 처리
   if character_y_pos < 0:
      character_y_pos = 0
   elif character_y_pos > screen_height - character_height:
      character_y_pos = screen_height - character_height

   screen.blit(background, (0, 0))  # (게임이 진행중인 동안) background이미지를 (0,0) 좌표에서 실행시킵니다)  # 배경그리기
   # 좌측 상단을 기준으로 좌표를 계산 (좌측최상단 = 0,0)
   screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
   pygame.display.update()  # 게임화면을 다시 그리기 (미호출시 반영이 되지 않음)
# pygame 종료
pygame.quit()