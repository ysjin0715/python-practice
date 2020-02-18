import turtle
import time

#2.애니메이션 만들기
t1=turtle.Turtle()
t1.shape('turtle')
s=int(turtle.textinput("",'당신의 국뽕의 크기를 넣어주세요'))

# def draw_shape():
#     t1.left(270)
#     t1.width(3)
#     t1.color('black','red')
#     t1.begin_fill()
#     t1.circle(s/2.0,-180)
#     t1.circle(s,180)
#     t1.left(180)
#     t1.circle(-s/2.0,-180)
#     t1.end_fill()
#     t1.color('black','blue')
#     t1.begin_fill()
#     t1.circle(s/2.0,-180)
#     t1.circle(s,-180)
#     t1.circle(s/2.0,180)
#     t1.end_fill()
#
# draw_shape()
# time.sleep(2)

def draw_shape_answer(color):
    t1.left(270)
    t1.width(3)
    t1.color('black',color)
    t1.begin_fill()
    t1.circle(s/2.0,-180)
    t1.circle(s,180)
    t1.left(180)
    t1.circle(-s/2.0,-180)
    t1.end_fill()

draw_shape_answer('red')
t1.setheading(180)
draw_shape_answer('blue')
time.sleep(2)