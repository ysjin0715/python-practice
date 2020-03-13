# self : 한 인스턴스가 객체 내 메소드를 호출할 때 self는 어느 인스턴스가 객체 내 메소드를 호출했는지 판별하는 역할을 한다.

class Car:
   def __init__(self, speed, color, model):
      self.speed = speed
      self.color = color
      self.model = model

   def drive(self):
      self.speed = 60

myCar = Car(0, 'blue', 'E-Class')
yourCar = Car(0, 'white', 'S-class')

myCar.drive()
print(myCar.speed)
