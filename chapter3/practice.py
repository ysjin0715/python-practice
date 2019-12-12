#1.
x=int(input('x: '))
y=int(input('y: '))

s=x+y
m=x-y
a=x*y
b=(x+y)/2

print('두수의 합: ',s)
print('두수의 차: ',m)
print('두수의 곱: ',a)
print('두수의 평균: ',b)
print('큰수: ',max(x,y))
print('작은수: ',min(x,y))

#2.
r=int(input('r: '))
h=int(input('h: '))
v=3.141592*r**2*h

print('원기둥의 부피: ',v)

#3.
c=input('정수를 입력하시오: ')
c_int=int(c)
sum=0
for i in range(len(c)):
    n=c_int%10
    c_int//=10
    sum=sum+n

print('자리수의 합: ',sum)

#4.
x1=int(input('x1: '))
x2=int(input('x2: '))
y1=int(input('y1: '))
y2=int(input('y2: '))

d=((x1-x2)**2+(y1-y2)**2)**0.5
print('두점 사이의 거리=',d)

#5.
import turtle
import time
t=turtle.Turtle()
t.shape("turtle")

t.left(45)
t.fd(d)
t.up()
t.goto(0,0)
t.setheading(0)

t.down()
t.fd(x2)
t.left(90)
t.fd(y2)
time.sleep(1)

#6.
x1=int(input('x1: '))
x2=int(input('x2: '))
y1=int(input('y1: '))
y2=int(input('y2: '))

d=((x1-x2)**2+(y1-y2)**2)**0.5

t.up()
t.goto(x1,y1)
t.down()
t.goto(x2,y2)
t.write(format('점의 길이=%f' % d))

time.sleep(1)
import time
f=time.time()

#7.
sec=f%60
m=f//60%60
h=f//60//60%24

print('현재 시간(영국 그리니치 시각): ',int(h),'시',int(m),'분')

#8.
weight=int(input('물체의 무게를 입력하시오(킬로그램): '))
speed=int(input('물체의 속도를 입력하시오(m/s) : '))
j=(1/2)*weight*speed**2

print('물체는',j,'(줄)의 에너지를 가지고 있다.')
