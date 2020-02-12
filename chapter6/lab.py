import turtle
import random
t=turtle.Turtle()
t.shape('turtle')

#1.
width=int(turtle.textinput("",'한 변의 길이'))

for i in range(3):
    t.fd(width)
    t.left(360/3)

t.up()
t.goto(200,0)
t.down()

for i in range(4):
    t.fd(width)
    t.left(360/4)

t.up()
t.goto(-200,0)
t.down()

for i in range(6):
    t.fd(width)
    t.left(360/6)

#2.
angle=int(turtle.textinput("",'몇각형을 원하시나요?'))
len=int(turtle.textinput("",'한 변의 크기는?'))
for a in range(angle):
    t.fd(len)
    t.left(360/angle)

#3.
for b in range(30):
    length = random.randint(1, 100)
    angle1 = random.randint(-180, 180)
    t.fd(length)
    t.left(angle1)

#adv3.
for c in range(30):
    length1=random.randint(1,100)
    angle2=random.randint(1,4)
    t.fd(length1)
    t.right(90*angle2)

#4.
num=int(input('정수를 입력하시오: '))
fact=1
for d in range(1,num+1):
    fact=fact*d
print(num,'!은',fact,'이다.')

5.
dan=int(input('원하는 단은: '))
for i in range(1,10):
    gob=dan*i
    print(dan,'*',i,'=',gob)

i=1
dan=1
while dan<=9:
    if i==10:
        i=1
        dan=dan+1
    else:
        print('%s*%s=%s'%(dan,i,dan*i))
        i=i+1


#6.
i=0
while i<5:
    t.fd(50)
    t.right(144)
    i=i+1

#7.
t.up()
t.goto(0,0)
t.down()

colorlist=['red','purple','blue','green','yellow','orange']
turtle.bgcolor('black')
t.speed(0)
t.width(3)
length1=10

while length1<500:
    t.fd(length1)
    t.pencolor(colorlist[length1%6])
    t.left(89)
    length1+=5

#8.
total=0
answer='yes'
while answer=='yes':
    number1=int(input('숫자를 입력하시오: '))
    answer=input('계속?(yes/no): ')
    total+=number1
print('합계는:',total)

#9.
start=0
print('1부터 100 사이의 숫자를 맞추시오')
answer1=random.randint(1,100)
guess=-1
while guess!=answer1 and start<10:
    guess=int(input('숫자를 입력하시오: '))
    start+=1
    if guess<answer1:
        print("큼!")
    if guess>answer1:
        print('작음!')

if start==10:
    print('정답은',answer1)

elif guess==answer1:
    print('축하합니다.','시도횟수=',start)

#10.
pluslist = ['+','-']
while True:
    x=random.randint(1,100)
    y=random.randint(1,100)
    math=random.randrange(2)
    answer2=int(input(str(x)+str(pluslist[math])+str(y)+'= '))
    if math==0:
        if x+y==answer2:
            print('참 잘했어요!')
        else:
            print('한심하군요. 다시 태어나세요')
    else:
        if x-y==answer2:
            print('참 잘했어요!')
        else:
            print('뺄셈도 못하면서 어떻게 살아가시려고요?')

#11.
bread=['호밀빵','위트','화이트']
meat=['미트볼','소시지','닭가슴살']
vege=['양상추','토마토','오이']
sau=['마요네즈','허니 머스타드','칠리']

for a in bread:
    for b in meat:
        for c in vege:
            for d in sau:
                print(a,'+',b,'+',c,'+',d)

#12.
t.color('red')
for i in range(12):
    t.up()
    t.goto(0,0)
    t.right(30)
    t.fd(30)
    t.down()
    t.fd(70)
    t.up()
    t.fd(30)
    t.stamp()

#13.
# -*- conding: utf-8 -*-
luckans=['무엇을 해도 다 되는 날입니다',
         '저주받은 날입니다. 외출을 삼가세요. 당장 죽어도 이상하지 않습니다.',
         '앞만 보고 가지 말고 뒤도 돌아보는 여유가 필요합니다',
         '자신의 일에 확신을 가지고 앞으로 나아가세요',
         '당신의 조력자가 당신에게 큰 도움을 줄 것입니다.',
         '주위 사람에게 언제든 칼을 찔려도 이상하지 않습니다',
         '당신의 실수를 운명의 탓으로 돌리지 마십시오. 당신의 능력을 탓해야합니다',
         '현재에서 벗어나 더욱 멀리 바라보아야 할 시점입니다.']
number123=random.randrange(len(luckans))
import sys

your_question=""
while True:
    name=input('이름: ')
    if name=="":
        sys.exit()
    your_question1=input('환영합니다!'+name+'님! 무엇에 대하여 알고 싶은가요? ')
    if your_question==your_question1:
        print('같은 거 묻지 마세요. 부정탑니다')
        sys.exit()
    print(name+'님,'+your_question1+'에 대해서 질문 주셨군요.')
    print('운명의 주사위를 돌려볼게요...')
    print(luckans[number123])
    your_question=your_question1
