#1.
age=30
if age<20:
    print('20살 미만')
else:
    print('20살 이상')

#출력값 : 20살 이상으로 출력

#2.
if age>=30 and age<=50:
    print('체크 가능합니다')
else:
    print('체크가 불가능합니다')

# 3.
warm=int(input('현재 온도를 입력하시오: '))
if warm>=25:
    print('반바지를 입으세요')
else:
    print('긴바지를 입으세요')

#4.
a=int(input('성적을 입력하시오: '))
if a>=90:
    print('A학점입니다.')
elif a>=80:
    print('B학점입니다.')
elif a>=70:
    print('C학점입니다.')
elif a>=60:
    print('D학점입니다.')
else:
    print('F학점입니다.')

#5.
import random
x=(random.randint(1,100))
y=random.randint(1,100)
answer=int(input(str(x)+'-'+str(y)+'= '))
if x-y==answer:
    print('맞았습니다')
else:
    print('틀렸습니다')

#6.
read=int(input('정수를 입력하시오: '))
if read%2==0 and read%3==0:
    print('2와 3으로 나누어떨어집니다')
else:
    print('불가능합니다')

#7.
magic_number=random.randint(0,99)
your_number=int(input('복권번호를 입력하시오: '))
print('당첨번호는 %d입니다'%magic_number)
digit1=magic_number//10
# 십의 자리
digit2=magic_number%10
#일의 자리
if your_number<=99:
    if your_number==magic_number or your_number==digit2*10+digit1:
        print('상금은 100만원입니다')
    elif your_number//10==digit1 or your_number//10==digit2:
        print('상금은 50만원입니다')
    elif your_number%10==digit1 or your_number%10==digit2:
        print('상금은 50만원입니다')
    elif your_number!=magic_number:
        print('상금은 없습니다')
else:
    print('올바른 번호를 입력하지 않았습니다. 돈을 회수합니다')

#8.
import time
import turtle
t=turtle.Turtle()
t.shape("turtle")
x1=int(input('큰 원의 중심좌표 x1: '))
y1=int(input('큰 원의 중심좌표 y1: '))
r1=int(input('큰 원의 반지름: '))
x2=int(input('작은 원의 중심좌표 x2: '))
y2=int(input('작은 원의 중심좌표 y2: '))
r2=int(input('작은 원의 반지름: '))

t.up()
t.goto(x1,y1)
t.down()

t.circle(r1)

t.up()
t.goto(x2,y2)
t.down()

t.circle(r2)

d=(((x1-x2)**2)+((y1-y2)**2))**0.5

if d+r2<=r1:
    t.write('두번째 원이 첫번째 원의 내부에 있습니다')
    time.sleep(2)
else:
    t.write('두번째 원이 첫번째 원 밖으로 나갔습니다')
    time.sleep(2)