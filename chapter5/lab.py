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

#7.
user_name='ilovepython'
user_pw='123456'
id=input('아이디를 입력하시오: ')
if id==user_name:
    pw=input('패스워드를 입력하시오: ')
    if pw==user_pw:
        print('환영합니다.')
    else:
        print('패스워드를 찾을 수 없습니다')
else:
    print('아이디를 찾을 수 없습니다')

# #8.
import random
kick_list=['왼쪽 상단','왼쪽 하단','중앙','오른쪽 상단','오른쪽 하단']
computer=random.choice(kick_list)
user_kick=input('어디로 공을 찰까요? (왼쪽 상단, 왼쪽 하단, 중앙, 오른쪽 상단, 오른쪽 하단) : ')
# if user_kick==kick_list[0] or user_kick==kick_list[1] or user_kick==kick_list[2] or user_kick==kick_list[3] or user_kick==kick_list[4]:
#     if user_kick==computer:
#         print('패널티킥이 막혔습니다!')
#     else:
#         print('패널티킥에 성공하셨습니다!')
# else:
#     print('올바른 방향에 차지 않았습니다')

if user_kick==computer:
    print('패널티킥이 막혔습니다!')
elif user_kick in kick_list:
    print('패널티킥이 성공했습니다!')
else:
    print('올바른 방향에 차십시오!')


# 9.
t.up()
t.goto(0,0)
t.down()
plist=['사각형','삼각형','원']
s=turtle.textinput("",'도형을 입력하시오: ')

if s in plist:
   if s=="사각형":
       c=90
       w = int(turtle.textinput("", "가로: "))
       h = int(turtle.textinput('', '세로: '))
       t.fd(w)
       t.left(c)
       t.fd(h)
       t.left(c)
       t.fd(w)
       t.left(c)
       t.fd(h)

   elif s=="삼각형":
       c=120
       w2=int(turtle.textinput('','한 변의 길이: '))
       t.fd(w2)
       t.left(c)
       t.fd(w2)
       t.left(c)
       t.fd(w2)
       t.left(c)

   elif s=="원":
       r=int(turtle.textinput('','반지름의 길이: '))
       t.circle(r)
else:
    print("해당 도형은 지원하지 않습니다.")