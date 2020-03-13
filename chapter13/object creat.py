# 객체를 생성/초기화하기
# __init__생성자 : 객체를 초기화한다. 객체를 생성 시 각 값을 받아 객체 내 변수에 저장한다.

class Car:
   def __init__(self, speed, color, model):          # 객체 초기화/ 객체 생성시 speed/color/model의 값을 받아 저장한다.
      self.speed = speed
      self.color = color
      self.model = model


   def drive(self):                                  # 메소드 생성
      self.speed = 60


myCar = Car(0, 'blue', 'E-class')                    # myCar라는 객체를 생성할 때 각각 speed, color, model의 값을 지정해준다.

print('자동차 객체를 생성하였습니다.')
print('자동차의 속도는',myCar.speed)                  # myCar 객체를 만들 때 지정해둔 값이 출력되는 걸 볼 수 있다.
print('자동차의 색상은',myCar.color)
print('자동차의 모델은',myCar.model)
print('자동차를 주행합니다.')

myCar.drive()                                        # myCar 내 메소드 호출 시 메소드 내 저장된 speed의 값으로 바뀌는 걸 볼 수 있다.
print('자동차의 속도는',myCar.speed)
