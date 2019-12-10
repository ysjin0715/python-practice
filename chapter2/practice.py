#1.
from datetime import datetime
now=datetime.now()
name=input('이름을 입력하시오: ')
age=int(input('나이를 입력하시오: '))
future=now.year+(100-age)
print(name,'씨는',future,'년에 100살이시네요!')

#2.
import math
x=int(input('첫 번째 숫자를 입력하시오: '))
y=int(input('두 번째 숫자를 입력하시오: '))
z=int(input('세 번째 숫자를 입력하시오: '))
sum=x+y+z
avg=sum/3

print(x,y,z,'의 평균은',avg,'입니다.')

#3.
r=int(input('반지름을 입력하시오: '))
pie=3.141592
circle=pie*r**2

print('반지름이',r,'인 원의 넓이 =',circle)

#4.
#그리기 관련 함수는 이걸로 사용하기
import turtle
t=turtle.Turtle()
t.shape("turtle")
t.width(3)
#반지름 초기값 설정
radius=50

#최초의 원 그리기
t.circle(radius)
#두번째 원 반지름 증가
radius=radius+20
#두번째 원 그리기
t.up()
t.goto(100,0)
t.down()
t.circle(radius)
#세번째 원 반지름 증가
radius=radius+20
#세번째 원 그리기
t.up()
t.goto(200,0)
t.down()
t.circle(radius)

#5.
#4번에서 옮겨졌던 위치 원래대로 돌려놓기
side=100
t.up()
t.goto(0,0)
t.down()

t.fd(side)
t.left(120)
t.fd(side)
t.left(120)
t.fd(side)
t.left(120)
#6. 'side'변수의 값만 200으로 설정하면 가능하다.
#7.
side=100
angle=90

t.fd(side)
t.left(angle)
t.fd(side)
t.left(angle)
t.fd(side)
t.left(angle)
#첫번째 사각형 완성

t.fd(side*2)
t.left(angle)
t.fd(side)
t.left(angle)
t.fd(side)
t.left(angle)
#두번째 사각형 완성

t.fd(side*2)
t.left(angle)
t.fd(side)
t.left(angle)
t.fd(side)
t.left(angle)
#세번째 사각형 완성

t.fd(side*2)
t.left(angle)
t.fd(side)
t.left(angle)
t.fd(side)