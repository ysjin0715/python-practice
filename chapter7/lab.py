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

# 4.
def draw(x,y):
    t.goto(x,y)

t.pensize(10)
s=turtle.Screen()
s.onscreenclick(draw)

s.onkey(t.penup,"Up")
s.onkey(t.pendown,'Down')
s.listen()

#5. 나무그리기
def tree(length):

    if length>50: #length가 5보다 크면 순환호출을 한다.
        t.fd(length) #거북이가 length만큼 선을 그린다.
        t.right(20) #오른쪽으로 20도 회전한다.
        tree(length-15) #(length-15)를 인수로 tree()를 순환 호출한다.

        t.left(40) #왼쪽으로 40도 회전한다.
        tree(length-15) #(length-15)를 인수로 tree()를 순환 호출한다.
        t.right(20) #오른쪽으로 20도 회전한다.

        t.backward(length) #length만큼 뒤로 간다. 제자리로 돌아온다.

t.left(90)
tree(90)

#6.막대그래프 그리기
def makdae(height):
    t.begin_fill()
    t.fd(50)
    t.left(90)
    t.fd(height)
    t.left(90)
    t.fd(50)
    t.write(str(height), font=('Times New Roman', 20, 'bold'))
    t.left(90)
    t.fd(height)
    t.left(90)
    t.end_fill()
    t.fd(50)


t.fillcolor('red')

t.up()
t.goto(-200,-200)
t.down()

data=[120,56,309,220,156,23,98]

for c in data:
    makdae(c)

# 7.터틀 메이즈 러너
def miro(x,y):
    for i in range(2):
        t.up()
        if i==1:
            t.goto(x+100,y+100)
        else:
            t.goto(x-100,y-100)
        t.down()
        t.fd(300)
        t.right(90)
        t.fd(300)
        t.left(90)
        t.fd(300)

def turn_left():
    t.left(10)
    t.forward(10)

def turn_right():
    t.right(10)
    t.fd(10)

miro(-200,200)
t.up()
t.goto(-200,200)
t.down()

screen=turtle.Screen()
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")
screen.listen()
screen.mainloop()
