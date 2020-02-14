# 3-4.함수 설정하기
def print_address():
    print('서울특별시 종로구 1번지')
    print('파이썬 빌딩 7층')
    print('홍길동')


print_address()
print_address()
print_address()


# 5.인수(홍길동)-매개변수(name변수) 간 관계 이해하기
def print_address(name):
    print('서울특별시 종로구 1번지')
    print('파이썬 빌딩 7층')
    print(name)


print_address('홍길동')


# 6. 반환 값 알아보기
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area


c_area = calculate_area(5.0)
print(c_area)
area_sum = calculate_area(5.0) + calculate_area(10.0)
print(area_sum)


# 7. 여러개의 값 반환하기
def git_input():
    return 2, 3


x, y = git_input()
print(x, y)


#7. 함수에 여러 개의 입력 전달하기
def get_sum(start, end):
    sum=0
    for i in range(start, end+1):
        sum+=i
    return sum

print(get_sum(1,10))

#8.지역변수와 전역변수
def calculate_area():
    result=3.14*r**2
    return result
#result=지역변수로, calculate area함수를 벗어나면 사용할 수 없음
#r=전역변수로, calculate area함수 밖에서 한계선을 설정해주었으므로 사용이 가능하다.
#즉, 함수 안에서 조건 설정 시 변수가 사용되었더라도, 함수 밖에서 그 변수에 대한 조건을 설정해준다면 전역변수가 된다.

r=float(input('원의 반지름: '))
area=calculate_area()
print(area)

#9.함수 안에서 전역변수를 사용해보자
#전역변수의 잘못된 사용 예시
def calculate_area(radius):
    area=3.14*radius**2
    return

area=0
r=float(input('원의 반지름: '))
calculate_area(r)
print(area)

#전역변수 사용의 잘된 예시
def calculate_area(radius1):
    global area
    area=3.14*radius1**2
    return

area=0
r1=float(input('원의 반지름: '))
calculate_area(r1)
print(area)
#global함수는 함수 내에서 전역변수를 생성할 수 있으며
#함수 안에서 전역변수의 값을 변경할 수도 있다.

#10. 디폴트 인수
#디폴트 인수를 지정하지 않을 때, 인수가 두 개 이상 필요한 함수의 경우 호출 시 반드시 두 개의 인수를 사용해서 호출해야한다.
def greet(name,msg):
    print("안녕 ",name,', ',msg)

greet('철수', '좋은 아침!')

#디폴트를 지정해주면, 인수가 두 개 이상 필요한 함수를 호출할 때 하나만 호출해도 나머지는 디폴트값이 빈자리를 채워준다.
def greet(name,msg='별일 없죠?'):
    print('안녕',name,',',msg)

greet('철수','좋은 아침!')
greet('영희')

#11.키워드 인수
def calc(x,y,z):
    return x+y+z

#일반적으로 x,y,z의 위치에 맞추어 값을 넣어주는 방법을 사용한다(위치인수)
calc(10,20,30)

#x,y,z의 값을 하나하나 지정하여 값을 넣어줄수도 있다. 이 경우, 기입위치가 바뀌더라도 키워드에 따라 값이 대입된다(키워드인수)
calc(x=10,y=20,z=30)
calc(y=20,x=10,z=30)

#위치인수와 키워드인수가 섞여서 사용해도 괜찮으나, 위치 인수가 키워드 인수 앞에 나와야 한다)
calc(10, y=20, z=30)