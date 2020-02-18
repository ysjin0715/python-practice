#3. 애스터로이드 게임
import turtle
import random
import math
player=turtle.Turtle()
player.color('green')
player.shape('turtle')
player.up()
player.speed(0)
screen=player.getscreen()
player.goto(0,0)

a1=turtle.Turtle()
a1.color('red')
a1.shape('circle')
a1.up()
a1.speed(random.randint(0,7))
x1=random.randint(-400,400)
y1=random.randint(-400,400)
a1.goto(x1,y1)

a2=turtle.Turtle()
a2.color('red')
a2.shape('circle')
a2.up()
x2=random.randint(-400,400)
y2=random.randint(-400,400)
a2.goto(x2,y2)

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def play():
    player.fd(20)
    a1.left(random.randint(0,360))
    a1.fd(15)
    a2.left(random.randint(0,360))
    a2.fd(15)
    screen.ontimer(play, 1)

screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.listen()
x3=player.xcor()
y3=player.ycor()
screen.ontimer(play,1)
screen.mainloop()