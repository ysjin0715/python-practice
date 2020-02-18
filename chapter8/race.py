#1.import random 함수 배우기
import random
import turtle
import time
#0.0부터 1.0보다 작은 실수 사이의 난수를 출력한다.
print(random.random())

#정수 구간의 난수 출력(randint(a,b): a<=N<=b)
print(random.randint(1,100))

#문자열이나 리스트 안에서 랜덤하게 하나의 항목을 선택: choice
print(random.choice('abcdefgh'))

#항목들 섞기
items=[1,2,3,4,5,6,7]
random.shuffle(items)
print(items)

#2. 거북이 경주게임
#거북이 두마리 생성해서 위치시키기
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t1.shape('turtle')
t2.shape('turtle')
t3.shape('turtle')


t1.up()
t2.up()
t3.up()
t1.goto(-400,0)
t2.goto(-400,-100)
t3.goto(-400,100)
t1.shapesize(5)
t2.shapesize(5)
t3.shapesize(5)
t1.color('pink')
t2.color('blue')
t3.color('green')
t1.pendown()
t2.pendown()
t3.pendown()
sum1=0
sum2=0
sum3=0


while True:
    d1=random.randint(0,60)
    d2=random.randint(0,60)
    d3=random.randint(0,60)
    t1.fd(d1)
    t2.fd(d2)
    t3.fd(d3)
    sum1+=d1
    sum2+=d2
    sum3+=d3

    if sum1>=400 or sum2>=400 or sum3>=400:
        print('경기가 끝났습니다.')
        if sum1>=400:
            print('우숭자는 분홍거북이입니다!')
        elif sum2>=400:
            print('우숭자는 파랑거북이입니다!')
        elif sum3>=400:
            print('우숭자는 방사능거북이입니다!')
        elif sum1==sum2 or sum2==sum3 or sum1==sum3:
            print('무승부입니다. 재경기를 진행해주세요')

        time.sleep(2)
        break
