#3-4.리스트 생성하기/.이 의미하는 것은?(모든 리스트는 객체이다)
#리스트 내부에 있는 개개별의 내용을 '항목(item)'이라고 한다.
number=[7, 12, 33, 777]
#공백의 리스트를 생성하는 것도 가능하다.
numbers=[]
print(numbers)
#공백의 리스트에 항목을 추가하기 위해서는 append를 이용한다.
#항목을 추가하려면 리스트가 먼저 생성되어야 한다.
numbers.append(560)
print(numbers)

numbers.append(740)
print(numbers)

#파이썬은 리스트 내부에 숫자, 문자열, 심지어는 다른 리스트도 항목으로 할 수 있다.
numbers.append(number)
numbers.append('문자열')
print(numbers)

#5.리스트의 항목 접근하기
#리스트에서 하나의 항목에 접근할 때는 항목의 인덱스(리스트에서의 항목의 위치(번호))를 이용한다.
letters=['a','b','c','d']
print(letters[0])

#6.슬라이싱(한번에 여러 개의 항목을 추출하는 기법)
#추출되는 항목의 개수는 두번째 인덱스에서 첫번째 인덱스를 뺀 값이다. (3-0)
print(letters[0:3])

#슬라이스를 더 간략하게 표현하기
#첫번째 인덱스를 생략할 경우 무조건 리스트의 첫번째로 인식한다.
print(letters[:3])

#두번째의 인덱스를 생략할 경우, 무조건 리스트의 끝까지라고 인식한다.
print(letters[3:])
#letters[:]를 이용하여 리스트의 복사본을 생성할 수 있다.
print(letters[:])


#7. 항목 변경하기
heros=['아이언맨','토르','헐크','스칼렛위치']
print(heros)
heros[1]='닥터 스트레인져'
print(heros)

#그러나 아직 존재하지 않는 인덱스를 이용하여 리스트에 항목을 추가할 수는 없다.
#함수를 사용하여 추가한다.
#첫번째 방법
heros.append('스파이더맨')
print(heros)
#두번째 방법
#insert(추가하고자 하는 위치(인덱스번호),'추가하고자 하는 내용')을 입력하면된다.
#항목의 갯수에 비해 터무니없이 인덱스의 숫자가 크면 가장 끝에 항목이 추가된다.
heros.insert(1,'배트맨')
print(heros)
heros.insert(10,'철갑맨')
print(heros)

#8. 항목 삭제하기
#첫번째 방법(remove)
#remove를 사용하면 항목의 위치를 알 필요가 없다. 단 리스트 내에 지시한 항목이 없을 경우 오류가 뜰 수 있다.
#그럴 경우 if문을 통해 오류를 없앤다.
heros.remove('철갑맨')
print(heros)
if '슈퍼맨' in heros:
    heros.remove('슈퍼맨')
print(heros)

#두번째 방법(del)
#del함수를 사용할 경우 인덱스번호를 지정하여 삭제한다.
del heros[0]
print(heros)

#세번째 방법(pop)
#pop함수는 무조건 마지막 항목을 삭제하여 반환한다.
heros.pop()
print(heros)

#9. 리스트 탐색하기
print(heros.index('헐크'))
if '배트맨' in heros:
    print(heros.index('배트맨'))

#리스트의 모든 항목을 한 번씩 방문하기
for hero in heros:
    print(hero)


#10. 리스트 정렬하기
#리스트 내 항목들을 크기순으로 나열할 수 있다.
print(heros)
heros.sort()
print(heros)

number=[1,3,5,6,2,0,4]
number.sort()
print(number)

#sort가 본래 리스트의 값을 바꾸는 데 반해 sorted는 기존의 값을 바꾸지 않는다.
number=[1,3,5,6,2,0,4]
sorted(number)
print(number)


#리스트 역으로 정렬하기
New_list=sorted(number,reverse=True)
print(New_list)

