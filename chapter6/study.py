#2.
print('방문을 환영합니다!')
print('방문을 환영합니다!')
print('방문을 환영합니다!')
print('방문을 환영합니다!')
print('방문을 환영합니다!')

# for i in range(1000):
#     print('방문을 환영합니다!')

#4.
for i in [1, 2, 3, 4, 5]:
    print('방문을 환영합니다')

#5.
for i in [1, 2, 3, 4, 5]:
    print("i=",i)

for a in [1, 2, 3, 4, 5]:
    print("9*",a,"=",9*a)

#6.
for b in range(5):
    print('방문을 환영합니다')

print(list(range(10)))

#7.
for i in range(1,6,1):
    print(i,end="")

for i in range(10,0,-1):
    print(i,end="")

#8.
import turtle
t=turtle.Turtle()
t.shape('turtle')

for count in range(6):
    t.circle(100)
    t.left(360/6)

#9.
response='아니'
while response=='아니':
    response=input('업마, 다됬어?');
print('먹자')

#10.
password=""
while password!='pythonisfun':
    password=input('암호를 입력하시오: ')
print('로그인 성공')

#11.
count=1
sum=0
while count<=10:
    sum=sum+count
    count=count+1
print('합계는',sum)\

#12.
t.up()
t.goto(0,0)
t.down()

i=0
while i<4:
    t.forward(100)
    t.right(90)
    i=i+1
#13.
while True:
    light=input('신호등 색상을 입력하시오: ')
    if light=='blue':
        break
print('전진!')