#1.
import turtle
t=turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(100,100)
t.write("거북이가 여기로 오면 양수입니다")
t.goto(100,0)
t.write("거북이가 여기로 오면 0입니다")
t.goto(100,-100)
t.write('거북이가 여기로 오면 음수입니다.')

t.goto(0,0)
t.pendown()
s=turtle.textinput("","숫자를 입력하시오: ")
n=int(s)
if(n>0):
    t.goto(100,100)
if(n==0):
    t.goto(100,0)
if(n<0):
    t.goto(100,-100)

#2.
age=int(input('나이를 입력하시오: '))
if(age>=15):
    print('이 영화를 보실 수 있습니다')
else:
    print('이 영화를 보실 수 없습니다')

#adv.2
age1=int(input('나이를 입력하시오: '))
if age1>=15:
    print('이 영화를 보실 수 있습니다.')
    print('영화의 가격은 10000원입니다.')

else:
    print('이 영화를 보실 수 없습니다.')
    print('다른 영화를 보시겠어요?')

#3.
t.up()
t.goto(0,0)
t.down()
t.shapesize(3,3)
t.width(3)


while True:

    order = input("명령을 입력하시오: ")

    if order=='l':
        t.left(90)
        t.forward(100)

    if order=='r':
        t.right(90)
        t.forward(100)

    if order=='q':
        print('프로그램을 종료합니다')
        break
#5.
year=int(input('연도를 입력하시오: '))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,'년은 윤년입니다.')
else:
    print('아닙니다')
#6.
import random
print("동전 던지기 게임을 시작합니다")
screen=turtle.Screen()
image1='../assets/CoinFront.gif'
image2='../assets/CoinBack.gif'
screen.addshape(image1)
screen.addshape(image2)

coin=random.randrange(2)
if coin==0:
    t.shape(image1)
    t.stamp()
    print('앞면입니다.')
else:
    t.shape(image2)
    t.stamp()
    print('뒷면입니다.')
import time
time.sleep(2)
print('게임을 종료합니다')
