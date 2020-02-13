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