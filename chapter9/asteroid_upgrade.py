#애스터로이드 게임
import turtle
import random
t=turtle.Turtle()
t.shape('turtle')
t.up()
screen=t.getscreen()

asteroids=[]
for i in range(10):
    a1=turtle.Turtle()
    a1.color('red','red')
    a1.shape('circle')
    a1.penup()
    a1.speed(0)
    a1.goto(random.randint(-300,300),random.randint(-300,300))
    asteroids.append(a1)

def turnleft():
    t.left(30)

def right():
    t.right(30)

def play():
    t.fd(2)
    for a in asteroids:
        a.right(random.randint(-180,180))
        a.fd(2)
    screen.ontimer(play,10)
screen.ontimer(play,10)

screen.onkeypress(turnleft,"Left")
screen.onkeypress(right,"Right")
screen.listen()
screen.mainloop()