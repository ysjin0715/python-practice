import turtle
t=turtle.Turtle()
t.shape('turtle')
import time

#1.사각형을 그리는 함수 작성하기
def square(length):
    for i in range(4):
        t.fd(length)
        t.left(90)

def square_plus(lengtha,angle):
    for i in range(angle):
        t.fd(lengtha)
        t.left(360/angle)

t.up()
t.goto(0,0)
t.down()
square_plus(100,7)

t.up()
t.goto(200,0)
t.down()
square_plus(100,5)

t.up()
t.goto(-200,0)
t.down()
square_plus(100,9)
time.sleep(2)

#2.n각형을 그리는 함수 작성하기
def n_polygon(n,length):
    for i in range(n):
        t.fd(length)
        t.left(360//n)

for a in range(10):
    t.left(20)
    n_polygon(6,100)

time.sleep(2)

#3.클릭하는 곳에 사각형 그리기
def square(length):
    for i in range(4):
        t.fd(length)
        t.left(90)

def drawit(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color('green')
    #square(50)
    t.circle(100)
    t.end_fill()

s = turtle.Screen()
s.onscreenclick(drawit)
#pycharm에서는 정상적으로 작동하지 않는다.
#python에서는 정상적으로 작동한다.

#4.
def draw(x,y):
    t.goto(x,y)
    t.pendown()

t.pensize(10)
s=turtle.Screen()
s.onscreenclick(draw)

s.onkey(t.penup,"Up")
s.onkey(t.pendown,'Down')
s.listen()

#5. 나무그리기
t.left(90)
def draw_tree(length):
    t.fd(length)
    t.left(180)
    t.fd(length/2)

    t.left(120)
    t.fd(length/2)
    t.left(180)
    t.fd(length/2)

    t.right(60)
    t.fd(length/2)
    t.right(180)
    t.fd(length/2)


draw_tree(100)