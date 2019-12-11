#1.
r=int(input('원하는 크기를 작성하시오: '))
a=int(input('몇각형을 그리시겠어요? '))
angle=180-(180*(1-(2/a)))
print(angle)

import time
import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(a):
    t.fd(r)
    t.left(angle)
    time.sleep(1)
    #t.left(360//a)가 더 간단함

#2.
merry_price=2000
latte_price=3000
chino_price=3500

count_merry=int(input('아메리카노 판매 개수: '))
count_latte=int(input('카페라테 판매 개수: '))
count_chino=int(input('카푸치토 판매 개수: '))

all=(count_merry*merry_price)+(count_latte*latte_price)+(chino_price*count_chino)
print('총 매출은',all,'입니다')

#3.
f=int(input('화씨온도: '))
c=(f-32)*(5/9)
print('섭씨온도:',c)

#4.
gram=float(input('몸무개를 kg 단위로 입력하시오: '))
tall=float(input('키를 미터 단위롤 입력하시오: '))
bmi=gram/(tall**2)
print('당신의 BMI=',bmi)

#5.
money_in=int(input('투입한 돈: '))
price=int(input('물건값: '))
money_out=money_in-price
print('거스름돈:',money_out)
print('500원 동전의 개수:',money_out//500)
print('100원 동전의 개수:',money_out%500//100)
print('10원 동전의 개수:',money_out%500%100//10)

#6.
x=int(input('첫 번째 수를 입력하시오:'))
y=int(input('두 번째 수를 입력하시오:'))
z=int(input('세 번재 수를 입력하시오:'))

avg=(x+y+z)/3
print('평균=',avg)