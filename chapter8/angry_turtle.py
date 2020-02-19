#4.앵그리터틀
import turtle
import math

player=turtle.Turtle()
player.shape('turtle')
screen=player.getscreen()
#
#거북이가 움직이는 좌표를 goto로 하므로 x값이 음수가 될 경우 거북이의 비행경로가 오류날 수 있다.
# player.up()
# player.goto(-200,0)
# player.down()

def turnleft():
    player.left(5)

def turnright():
    player.right(5)

def fire():
    x=0
    y=0
    angle=player.heading()
    # velocity=50
    velocity = int(turtle.textinput("", '거북이를 어느 속도로 던질꺼야? (*너무 세게 던지면 거북이가 아파한다구!)'))
    vx = velocity * math.cos(angle * 3.14 / 180.0)
    vy = velocity * math.sin(angle * 3.14 / 180.0)
    print(vx,vy)
    while player.ycor()>=0:
        vx=vx
        vy=vy-10
        x=x+vx
        y=y+vy
        player.goto(x,y)



screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.onkeypress(fire,"space")
screen.listen()


screen.mainloop()
