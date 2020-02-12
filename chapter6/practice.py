import turtle
t=turtle.Turtle()
t.shape('turtle')
import random
import time
import math

#1.
for i in range(1,101):
    if i%2==0:
        print(i,end=" ")
print('')

#2.
year=0
balance=1000

while balance <=2000:
    year+=1
    interest=balance*0.07
    balance+=interest
print(year,'년이 걸립니다')

#3.
n=1234
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
    print(digit)
print(sum)

#4.
x=random.randrange(10)
y=random.randrange(10)
while True:
    ans = int(input(str(x) + '*' + str(y) + '='))
    if x*y==ans:
        print('맞았습니다.')
        break

#5.
sum=0
while True:
    z=int(input('정수를 입력하시오: '))
    sum+=z
    if z==0:
        print('합은',sum,'입니다.')
        break

#6.
d1=0
d2=0
while d1!=6 or d2!=6:
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print('첫번째 주사위=',d1,' 두번째 주사위=',d2)

#7.
for i in range(6):
    t.up()
    t.home()
    t.down()
    t.right(60 * i)
    t.fd(100);t.fd(-30);t.left(60);t.fd(30);t.fd(-30);t.right(120);t.fd(30);t.fd(-30)

time.sleep(2)

#8.
t.color('red')
for a in range(10):
    for b in range(5):
        t.fd(-200)
        t.right(144)
    t.up()
    t.left(10)
    t.down()

#9.
t.home()
for d in range(10):
    t.up()
    r = random.randint(1, 100)
    x1 = random.randint(-300, 300)
    y1 = random.randint(-300, 300)
    t.goto(x1,y1)
    t.down()
    t.circle(r)

#10.
t.up()
t.goto(-200,200)
t.down()
for e in range(10):
    t.fd(400)
    t.right(90)
    t.fd(50)
    t.right(90)
    t.fd(400)
    t.left(90)
    t.fd(50)
    t.left(90)

#11.
t.color('red','yellow')
t.begin_fill()
while True:
    t.fd(200)
    t.left(170)
    print(abs(t.pos()))
    print(t.pos())
    if abs(t.pos())<1:
        break
t.end_fill()

#12.
t.home()
for f in range(360):
    degree = math.sin(f / 15) * 3600
    t.goto(f, 3.14*degree/180)

