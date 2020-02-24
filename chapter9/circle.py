#2. 오륜기 그리기
import turtle
t=turtle.Turtle()
t.shape('turtle')

color=[]
for i in range(5):
    s=turtle.textinput('','오륜기에 넣을 색을 입력하시오(영어가 아니면 인식하지 못한다구!')
    color.append(s)

# color.append('red')
# color.append('orange')
# color.append('yellow')
# color.append('blue')
# color.append('purple')

t.up()
t.goto(-200,0)
t.down()

def circle():
    for i in range(3):
        t.fillcolor(color[i-1])
        t.color(color[i-1])
        t.begin_fill()
        t.circle(100)
        t.end_fill()
        t.up()
        t.fd(200)
        t.down()
    t.up()
    t.goto(-100,-200)
    t.down()
    for g in range(2):
        t.fillcolor(color[g+2])
        t.color(color[g+2])
        t.begin_fill()
        t.circle(100)
        t.end_fill()
        t.up()
        t.fd(200)
        t.down()

circle()

# #position에서 리스트를 지정할 때, 리스트 내 리스트 형식으로 구성한다.
# #[x좌표,y좌표,'색깔']
# for x,y,c in position:
#     t.up()
#     t.goto(x,y)
#     t.pendown()
#     t.color(c,c)
#     t.begin_fill()
#     t.circle(30)
#     t.end_fill()
