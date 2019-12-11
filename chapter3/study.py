#덧셈
print(5+3)
#뺄셈
print(5-3)
#곱셈
print(5*3)
#나눗셈(몫의 값만 출력)
print(5//3)
#나눗셈(전체 값을 온전히 출력)
print(5/3)
#나머지 값만 출력
print(5%3)

#몫과 나머지를 계산한느 코드 작성
p=int(input("분자를 입력하시오: "))
q=int(input("분모를 입력하시오: "))
print("나눗셈의 몫=",p//q)
print("나눗셈의 나머지=",p%q)

#홀수와 짝수를 판별하는 계산
number=int(input("정수를 입력하시오: "))
print(number%2)

#초 환산 계산
sec=int(input("환산을 원하는 초를 입력하시오: "))
min=sec//60
remainder=sec%60
print(min,'분',remainder,'초 입니다.')

#지수연산자
a=1000
r=0.05
n=10
print(a*(1+r)**n)

#복합연산자
x=1000
print('초깃값x=',x)

x+=2
print('x+=2 후의 x=',x)

x-=2
print('x-=2후의 x=',x)