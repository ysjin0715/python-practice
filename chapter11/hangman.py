# 행맨만들기
from random import *

guesses = ''                                                # 사용자가 제출한 정답지
turns = 10                                                  # 사용자가 지닌 기회

infile = open('letter.txt','r',encoding = 'utf8')           # 문제파일 읽어들이기
lines = infile.readlines()                                  # 문제파일을 한 개씩 읽기 (readlines로 할 경우, 리스트형태로 나옴)
word = choice(lines).rstrip()                               # 임의로 출력된 단어에서 우측 여백을 제외함


while turns > 0:                                            # 기회가 남았을 경우
   failed = False
                                                            # <사용자가 정답을 맞추었는가?>
   for char in word:                                        # word를 char 변수에 대입하여
      if char in guesses:                                   # 만일 사용자가 제출한 정답지 안에 char가 포함되어 있다면?
         print(char, end="")                                # char를 출력한다.
      else:                                                 # 만일 사용자가 제출한 정답지 안에 char가 포함되어 있지 않다면?
         print('-',end="")                                  # -로 출력한다.
         failed = True

   if failed is False:
      print('\n사용자 승리')                                 # 사용자 승리를 출력하고 조건문에서 나가진다.
      break


   print('')                                                
   guess = input('단어를 추측하시오: ')                      # 사용자의 입력을 받아 guess에 저장한다.
   guesses += guess                                         # 사용자가 제출한 정답지에 사용자의 입력을 저장한다.
   if guess not in word:                                    # 만일 사용자가 입력한 내용이 단어에 없다면?
      turns -= 1                                            # 지닌 기회에서 하나를 빼고 '틀렸음!'을 출력한다.
      print("틀렸음!")
      print(str(turns)+'기회가 남았음!')                     # 현재 남은 기회 + 기회가 남았음을 출력한다.
      if turns == 0:                                        # 만일 기회가 0이 된다면?
         print('사용자 패배, 정답은 '+word)                  # 사용자가 패배했다는 메세지와 함께 정답을 공개한다.

infile.close()