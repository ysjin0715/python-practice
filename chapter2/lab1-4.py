#공통사항
import turtle
t=turtle.Turtle()
t.shape('turtle')

#lab1. 변수는 어디에 유용할까?
radius=100
#반지릅을 변경하기 위해서는 변수인 radius값을 변경한다.
radius=radius/2
t.circle(radius)
t.fd(30)
t.circle(radius)
t.fd(30)
t.circle(radius)

#lab2. 집 그리기
x=int(input('집의 크기는 얼마인가요? '))
t.fd(x)
t.left(120)
t.fd(x)
t.left(120)
t.fd(x)
#지붕 완성
t.left(30)
t.fd(x)
t.left(90)
t.fd(x)
t.left(90)
t.fd(x)
t.left(90)
#하단부 완성

#lab3. 로봇 기자 만들기
a=input('경기장은 어디입니까?')
b=input('이긴팀은 어디입니까?')
c=input('진팀은 어디입니까?')
d=input('우수선수는 누구입니까?')
e=input('스코어는 몇대몇입니까?')
#변수 입력창
print("")
print("===========================================")
print('오늘',a,'에서 야구 경기가 열렸습니다.')
print(b,'과',c,'은 치열한 공방전을 펼쳤습니다.')
print(d,'이 맹활약을 하였습니다')
print('결국',b,'가',c,'를',e,'로 이겼습니다.')
print("===========================================")


#lab4. 부동산 광고 만들기
street='서울시 종로구'
type='아파트'
number_of_rooms=3
price=100000000
print("")
print("########################################")
print("#                                      #")
print("#           부동산 매물 광고            #")
print("#                                      #")
print("########################################")

print(street,'에 위치한 아주 좋은',type,'가 매물로 나왔습니다. 이',type,'는',number_of_rooms,'개의 방을 가지고 있으며 가격은',price,'입니다.')

