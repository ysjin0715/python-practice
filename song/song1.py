import pygame
import time

pygame.mixer.init()

class song():
   def __init__(self, take, idol, file_directory, play_list):
      self.take = take
      self.idol = idol
      self.file_directory = file_directory
      self.play_list = play_list

   def play(self):
      index = 0
      start_time = time.time()
      end_time = start_time + (self.take[len(self.take) - 1])
      current_time = time.time()
      pygame.mixer.set_num_channels(10)

      sounds = []
      for i in range(0, 10):
         sounds.append(pygame.mixer.Sound(open(self.file_directory + "/" + self.play_list[i], 'rb')))

      for i in range(0, 10):
         pygame.mixer.Channel(i).play(sounds[i])

      for i in range(0, 10):
         pygame.mixer.Channel(i).set_volume(0)

      # pygame.mixer.music.play()

      while True:
         if index >= len(self.take):
            break
         print(current_time, index, ":::::::::::", self.idol[index], ":::::::", current_time - start_time)

         pygame.mixer.music.get_busy()
         current_time = time.time()

         for idol_index in self.idol[index]:
            pygame.mixer.Channel(idol_index).set_volume(100)

         if current_time - start_time > self.take[index]:
            for idol_index in self.idol[index]:
               pygame.mixer.Channel(idol_index).set_volume(0)
            index += 1


def get_idol():
   # 자리지정
   song_dic = {
      "호노카": "1_Honoka.wav",
      "하나요": "2_Hanayo.wav",
      "에리": "3_Eli.wav",
      "마키": "4_Maki.wav",
      "코토리": "5_Kotori.wav",
      "니코": "6_Niko.wav",
      "노조미": "7_Nozomi.wav",
      "린": "8_Rin.wav",
      "우미": "9_Umi.wav"
   }

   play_list = ["0_All.wav"]
   for i in range(1, 10):
      x = input("자리%d 에 위치할 아이돌의 이름을 적어주세요 : " % i)
      play_list.append(song_dic.get(x))

   return play_list


def get_song(name):
   idol = get_idol()

   # 각 곡의 시간대 및 포지션 설정 (커스텀)
   # Take 리스트와 idol_order의 길이는 같아야 함
   # 포지션 설정은 합주도 가능하도록 설정 가능 (이중리스트 활용)
   if name == 'snowhalation':
      # take = [22.80, 34.00, 40.20, 45.50, 49.80, 94.30, 105.44, 117.20, 123.60, 129.20, 133.31, 172.80, 196.00, 199.885, 260.00]
      take = [22.80, 34.00, 40.20, 49.80, 94.30, 105.44, 117.20, 123.60, 129.20, 172.80, 196.00, 199.885, 260.00]

      # idol_order = [[4, 5, 6], [1, 2, 3], [7, 8, 9], [1, 2, 3, 7, 8, 9], [4, 5, 6], [0], [7, 8, 9], [1, 2, 3], [7, 8, 9], [1, 2, 3, 7, 8, 9], [4, 5, 6], [0], [5], [4, 5, 6], [0]]
      idol_order = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [1], [2], [3], [4]]

      return song(take, idol_order, name, idol)

   pygame.mixer.music.play()



s = get_song("snowhalation")
s.play()