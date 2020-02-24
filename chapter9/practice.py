#1.
def practice1():
    number=[]
    number.append(int(input('정수를 입력하시오: ')))
    number.append(int(input('정수를 입력하시오: ')))
    number.append(int(input('정수를 입력하시오: ')))
    number.append(int(input('정수를 입력하시오: ')))
    number.append(int(input('정수를 입력하시오: ')))
    sum=0
    for i in range(len(number)):
        sum+=number[i]

    print('평균: ',sum/int(len(number)))


#2.
def practice2():
    import random
    import sys
    p=[0,0,0,0,0,0]
    while True:
        v=0
        s=input('주사위를 던지시겠습니까?(y/n): ')
        if s=="y":
           v=random.randint(1,6)
           p[v-1]+=1
           print('나온 주사위는 ',v,'입니다')
           print('무사히 주사위를 던졌습니다')

        elif s=='n':
            print('주사위가 1인 경우는 ', p[0])
            print('주사위가 2인 경우는 ', p[1])
            print('주사위가 3인 경우는 ', p[2])
            print('주사위가 4인 경우는 ', p[3])
            print('주사위가 5인 경우는 ', p[4])
            print('주사위가 6인 경우는 ', p[5])

        else:
            print('당신은 결과를 볼 자격도 없습니다')
            print('프로그램을 종료합니다')
            sys.exit()


#3.
def practice3():
    import sys
    number_book={}
    while True:
        name=input('(입력모드) 이름을 입력하시오: ')
        if name=="":
            while True:
                s_name = input('(검색모드) 이름을 입력하시오: ')
                if s_name == "":
                    print('프로그램을 종료합니다')
                    sys.exit()

                print(s_name,'의 전화번호는',number_book[s_name],'입니다')

        number=input('전화번호를 입력하시오: ')
        number_book[name]=number


#4.
def practice4():
    import turtle
    import random
    t=turtle.Turtle()
    t.shape('turtle')

    color=['purple','red','yellow','blue']
    b=len(color)

    def draw(d):
        for a in range(4):
            t.fd(d)
            t.left(90)

    for i in range(b):
        x=random.randint(-300,300)
        y=random.randint(-300,300)
        t.up()
        t.goto(x,y)
        t.down()

        t.color(color[i],color[i])
        t.begin_fill()
        draw(100)
        t.end_fill()


#5.
def practice5():
    import turtle
    import random
    t=turtle.Turtle()
    t.shape('turtle')

    color=['blue','green','skyblue','orange']

    def draw_anything():
        c = int(turtle.textinput('', '원하는 다각형을 입력하시오(숫자만 입력할 수 있다구!)'))
        for a in range(c):
            t.fd(100)
            t.left(360/c)

    f=len(color)

    for e in range(f):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)

        t.up()
        t.goto(x,y)
        t.down()

        t.color(color[e],color[e])
        t.begin_fill()
        draw_anything()
        t.end_fill()


def practice6():
    import turtle
    import random
    t=turtle.Turtle()
    t.shape('turtle')
    turtle.bgcolor('black')


    color=['orange','white','blue','skyblue','yellow']

    def draw_star():
        a=random.randrange(50,150)
        for b in range(5):
            t.fd(a)
            t.right(144)

    f = len(color)

    for e in range(f):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)

        t.up()
        t.goto(x, y)
        t.down()

        t.color(color[e], color[e])
        t.begin_fill()
        draw_star()
        t.end_fill()


#7
def practice7():
    domain={'kr':'대한민국','sk':'슬로바키아','no':'노르웨이','us':'미국','jp':'일본','hu':'헝가리','de':'독일'}

    for k in domain:
        print(k,': ',domain[k])


#8.
def practice8():
    import random
    import sys
    problom={'현현':'마음에 걸리는 바가 있음','고즈넉이':'고요하고 아늑한 상태로','허우대':'겉으로 드러난 체격','윤슬':'햇빛이나 달빛에 비치어 반짝이는 잔물결'}
    q=list(problom.values())
    s=list(problom.keys())
    count=3
    for i in range(count):
        b=int(len(q))
        a=random.randrange(b)
        print('다음은 무엇에 대한 설명인가')
        print(q[a])
        for c in range(b):
            print('(',c+1,')',sep="",end="")
            print(s[c],end=" ")
        print()
        d=input('정답을 입력하시오(한글로 입력해주라구!): ')
        if d==s[a]:
            count-=1
            print('정답입니다!')
            if count==0:
                print('축하합니다! 당신은 한국 유치원생의 어휘수준을 가지고 있습니다!')
                sys.exit()
            print('앞으로',count,'번 남았다구!')
        else:
            print('당신은 한국인이 아닙니다')
            print('한국국적이 어울리지 않습니다')
            sys.exit()

