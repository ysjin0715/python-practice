import turtle
import time
import random
t=turtle.Turtle()
t.shape('turtle')

#1.눈사람 그리기
s=turtle.Screen()
turtle.bgcolor('skyblue')

def draw_snowman(x,y):
    t.fillcolor('white')
    t.penup()
    t.goto(x,y)
    t.pendown()
    #머리 그리기
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    #머리와 몸통 겹치기
    t.left(90)
    t.fd(5)
    t.backward(25)
    #몸통 그리기
    t.begin_fill()
    t.right(90)
    t.circle(15)
    t.end_fill()
    #팔 두개 그리기
    t.right(90)

    for i in range(2):
        t.left(120)
        t.fd(70)
        t.backward(70)

    #아랫도리 그리기
    t.right(60)
    t.fd(10)
    t.begin_fill()
    t.left(90)
    t.circle(40)
    t.end_fill()

    #원점으로 돌리기
    t.right(180)


for i in range(3):
    x = random.randrange(-100, 100)
    y = random.randrange(-100, 100)
    draw_snowman(x,y)

#2. 벌집그리기
def hexagon():
    for i in range(6):
        t.left(360/6)
        t.fd(100)

t.fd(100)
t.right(360/6)

for i in range(6):
    t.fd(100)
    hexagon()
    t.right(360/6)

#3. 함수 그래프 그리기
t.up()
t.goto(0,0)
t.down()
t.fd(200)
t.backward(200)
t.left(90)
t.fd(200)
t.backward(200)
t.right(90)

def hamsu(x,y):
    t.goto(x,y)

for x in range(150):
    y = x * x + 1
    hamsu(x,y*0.01)

#4. 움직이지 않고 선긋기
def draw_line():
    turtle.fd(100)
    turtle.backward(100)

for i in range(12):
    turtle.right(30)
    draw_line()

#5. 매개변수를 이용하여 생일축하 노래부르기
def happyBirthday(name):
    print('Happy Birthday to you!')
    print('Happy Birthday to you!')
    print('Happy Birthday, dear '+name)
    print('Happy Birthday to you!')


happyBirthday(input('생일축하 주인공을 적어봐 : '))

#6. 2개의 정수를 받아서 수학문제 출력
def math_test(x,y):
    a=input('정수'+str(x)+'+'+str(y)+'의 합은?')
    if x+y==int(a):
        print('맞았습니다')
    else:
        print('당신은 사람이 아닙니다')

x=int(input('첫 번재 정수: '))
y=int(input('두 번째 정수: '))
math_test(x,y)

#7.
PI=3.14159265358797
def circleArea(radius):
    c=PI*radius*radius
    print('반지름이 ',str(radius)+'인 원의 면적:'+str(c))

def circleCircumference(radius):
    d=2*PI*radius
    print('반지름이 '+str(radius)+'인 원의 둘레:'+str(d))

circleArea(5)
circleCircumference(5)

#8. 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하는 함수를 각각 작성하고 테스트하기
def add1():
    x=random.randint(1,100)
    y=random.randint(1,100)
    a=int(input(str(x)+'+'+str(y)+'='))
    if a==x+y:
        print('사람입니다!')
    else:
        print('사람이 아닙니다')

def add2():
    x=random.randint(1,100)
    y=random.randint(1,100)
    a=int(input(str(x)+'-'+str(y)+'='))
    if x-y==a:
        print('사람입니다.')
    else:
        print('동물 취급하기에도 부끄럽습니다')

def add3():
    x=random.randint(1,100)
    y=random.randint(1,100)
    a=int(input(str(x)+'*'+str(y)+'='))
    if x*y==a:
        print('사람입니다')
    else:
        print('사람이 아닙니다')

def add4():
    x=random.randint(1,10)
    y=random.randint(1,10)
    a = float(input(str(x*10) + '/' + str(y*10) + '='))
    if (x*10)/(y*10)==a:
        print('정답')
    else:
        print('사람이 아닙니다.')


add1()
add2()
add3()
add4()
