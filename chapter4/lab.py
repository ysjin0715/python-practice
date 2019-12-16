import turtle
t=turtle.Turtle()
t.shape("turtle")

#1
s=turtle.textinput('','이름을 입력하십시오: ')
t.write('안녕하세요? %s씨, 터틀 인사드립니다.' %s)
a=4

for i in range(a):
    t.fd(100)
    t.left(90)

2.
print('안녕하세요?')
name=input('이름이 어떻게 되시나요?')

print('만나서 반갑습니다 %s씨'%name)
print('이름의 길이는 다음과 같군요: ',len(name))

age=int(input('나이가 어떻게 되나요?'))
print('내년이면 '+str(age+1)+ ' 이 되시는군요.')

#3.
year=int(input('오늘의 연도를 입력하시오: '))
month=int(input('오늘의 월을 입력하시오: '))
day=int(input('오늘의 일을 입력하시오: '))
print('오늘은',str(year),'년 ',str(month),'월 ',str(day),'일입니다.')

#4.
import time
now=time.time()
thisYear=int(1970+now//(365*24*3600))
print('올해는 ',str(thisYear),'입니다.')
age=int(input('몇 살이신지요? '))
future=2050-thisYear
fage=future+age
print('2050년에는',str(fage),'살 이시군요.')\


#5.
list_name=[]
list_name.append(input('친구의 이름을 입력하시오: '))
list_name.append(input('친구의 이름을 입력하시오: '))
list_name.append(input('친구의 이름을 입력하시오: '))
list_name.append(input('친구의 이름을 입력하시오: '))
list_name.append(input('친구의 이름을 입력하시오: '))

print(list_name)
print(list_name[0])

#6.
color_list=['yellow','red','blue','green']

#첫번째 원 완성
t.fillcolor(color_list[0])
t.begin_fill()
t.circle(100)
t.end_fill()

#이동
t.goto(40,0)

#두번째 원 완성
t.fillcolor(color_list[1])
t.begin_fill()
t.circle(100)
t.end_fill()

#이동
t.goto(80,0)

#세번째 원 완성
t.fillcolor(color_list[2])
t.begin_fill()
t.circle(100)
t.end_fill()

#이동
t.goto(120,0)

#네번째 원 완성
t.fillcolor(color_list[3])
t.begin_fill()
t.circle(100)
t.end_fill()