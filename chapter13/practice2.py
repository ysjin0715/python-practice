# TV를 클래스로 정의하자.
# Tv클래스는 다음과 같은 변수들과 함수들을 가진다. TV클래스의 객체를 생성하고 테스트해보자
# 채널(channel), 볼륨(volume), 전원상태(on), TurnOn() : TV를 켠다, TurnOff() : TV를 끈다, setChannel(channel) : 채널을 변경한다, setVolume(volume) : 볼륨을 변경한다.

class TV:
   def __init__(self, channel, volume, on):
      self.channel = channel
      self.volume = volume
      self.on = on

   def TurnOn(self):
      if self.on == True:
         print('TV가 이미 작동중입니다.')
      else:
         self.on = True
         print('TV가 작동합니다.')
         return self.on

   def TurnOff(self):
      if self.on == True:
         self.on = False
         print('TV가 꺼졌습니다.')
         return self.on
      else:
         print('TV가 이미 꺼졌습니다.')

   def setChannel(self):
      a = int(input('변경하실 채널 번호를 적으십시오 : '))
      if self.channel == a:
         print('현재 시청중인 채널입니다.')
      else:
         self.channel = a
         print('{0}채널로 변경이 완료되었습니다.'.format(self.channel))
         return self.channel

   def setVolumn(self):
      v = int(input('변경하실 볼륨 크기를 적으십시오 : '))
      if self.volume == v:
         print('현재 적용중인 볼륨입니다.')
      elif v >= 0:
         self.volume = v
         print('{}로 볼륨이 변경되었습니다.'.format(self.volume))
         return self.volume
      else:
         print('0 밑으로 볼륨을 적용할 수 없습니다.')


   def __str__(self):
      msg = 'TV의 채널: '+str(self.channel)+' TV의 음량: '+str(self.volume)
      return msg

t1 = TV(11,6,False)

print(t1)
t1.TurnOff()
t1.TurnOn()

t1.setChannel()
t1.setChannel()
print(t1)

t1.setVolumn()
t1.setVolumn()
t1.setVolumn()
print(t1)


