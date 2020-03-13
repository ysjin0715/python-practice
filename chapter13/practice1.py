# 원을 나타내는 클래스 circle을 정의해보자
# 반지름 = radius
# calcPerimeter() : 원의 둘래를 계산
# calcArea() : 원의 면적을 계산

class Circle():
   def __init__(self,radius):
      self.radius = radius
      print('반지름 : ',radius, end=" ")

   def calcPerimeter(self):
      result1 = 2 * 3.14 * self.radius
      print('원의 둘레 :', result1, end = " ")
      return result1


   def calcArea(self):
      result2 = 3.14 * self.radius**2
      print('원의 면적 :', result2, end = " ")
      return result2



c1 = Circle(5)
c1.calcArea()
c1.calcPerimeter()
