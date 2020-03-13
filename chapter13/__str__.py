# __str__() : str메소드를 정의할 경우, 객체 호출 시 객체 내 정보를 출력할 수 있도록 돕는다.
class Car:
   def __init__(self, speed, color, model):
      self.speed = speed
      self.color = color
      self.model = model

   def __str__(self):                                  # str메소드를 입력한다.
      msg = '속도:' + str(self.speed) + ' 색상:' + self.color + ' 모델:' + self.model
      return msg

myCar = Car(0, 'blue', 'E-Class')
print(myCar)                                           # str메소드 내 변수가 반환되며 출력된다.