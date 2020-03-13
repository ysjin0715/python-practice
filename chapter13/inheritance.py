# 상속 : 클래스를 정의 시 부모클래스를 지정해주는 것. 자식 클래스는 부모 클래스의 메소드와 변수를 사용할 수 있다.

from turtle import *

class MyTurtle(Turtle):                # Turtle 클래스를 상속받아서 MyTurtle클래스를 정의한다.
   def glow(self,x,y):
      self.fillcolor('red')

turtle = MyTurtle()                    # Turtle 클래스에게 상속받은 MyTurtle class의 인스턴스인 turtle 객체는 Turtle class의 모든 변수와 메소드를 사용할 수 있다.
turtle.shape('turtle')
turtle.onclick(turtle.glow)

