#1.
print('나는 '+str(12)+'개의 사과를 먹었다')

#2.
print('apple'+'grape')
print('apple'*3)

#3.
s=input('문자열을 입력하시오: ')
print(s[0:2]+s[-2:])

#4.
act=input("문자열을 입력하시오: ")
print(act+"하는 중")

#5.
sign=input("기호를 입력하시오: ")
text=input("중간에 삽입할 문자열을 입력하시오: ")
print(sign[0]+text+sign[-1])

#6.
listA=[1,2,3,4]
print('리스트 = ',listA)
sumA=listA[0]+listA[1]+listA[2]+listA[3]
print("리스트 숫자들의 합 = ",sumA)
#7.
colorA=input("색상 #1을 입력하시오: ")
colorB=input("색상 #2을 입력하시오: ")
colorC=input("색상 #3을 입력하시오: ")
listC=[colorA,colorB,colorC]

import turtle
t=turtle.Turtle()
t.shape("turtle")

for A in listC:
    t.fillcolor(A)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.up()
    t.forward(100)
    t.down()

# 8.
x1=int(input('x1 입력: '))
y1=int(input('y1 입력: '))
x2=int(input('x2 입력: '))
y2=int(input('y2 입력: '))
x3=int(input('x3 입력: '))
y3=int(input('y3 입력: '))

listB=[x1,y1,x2,y2,x3,y3]

t.up()
t.goto(0,0)
t.down()
# for i in range(3):
#     t.goto(listB[i*2],listB[i*2+1])
for i in range(0,5,2):
    t.goto(listB[i], listB[i + 1])