# 2. 연산자
## 2.1. 연산자
1. 사칙연산에 사용되는 모든 연산자
2. 특수 연산자
3. 비교 연산자

### 연산자의 종류 예시
**사칙연산 연산자**
```python
print(1+1) # 2
print(1-1) # 0
print(1*2) # 2
print(2/2) # 1
```
**특수 연산자**
1. 제곱
    ```python
    print(2 ** 3) # 2 * 2 * 2= 8
    ```
2. 나머지 출력
    ```python
    print(5%3) # 1...2=>2
    print(6%3) # 2...0=>0
    ```
3. 몫 출력
    ```python
    print(5//3) # 1...2=>1
    print(6//3) # 2...0=>2
    ```
**비교 연산자**
1. 크기비교
    ```python
    print(5>3)     # True
    print(6<3)     # False
    print(3>=2)    # True
    print(3<=2)    # False
    ```
2. 같은가?
    ```python
    print(3==3)        # True
    print(4==3)        # False
    print(3+4==7)      # True
    ```
3. 같지 않은가?
    ```python
    print(1!=3)        # True
    print(not(1!=3))   # not(True) #False
    ```

4. 복합 비교연산자

4.1. and

    ```python
    print((3>0) and (3<5))  # True and True=True
    print((3>0) & (3<5))    # True and True=True
    ```
    
4.2. or

    ```python
    print((3>0) or (1<5))   # A or B is True=True
    print((3>0) | (1<5))    # A or B is True=True
    ```
    
4.3. 연속 비교연산

    ```python
    print(3<4<5)    # True
    print(3>4>6)    # False
    ```

## 2.2. 간단한 수식
1. 일반적인 수식
    ```python
    print(2+3*4)   # 14
    print((2+3)*4) # 20
    
    #변수에 간단한 수식을 저장하여 출력할 수 있다.
    num = 2+3*4
    print(num)     # 14
    ```

2. 거듭해서 사칙연산하기
    ```python
    num=14
    num=num+2  #=num+=2
    print(num) #16
    
    num-=2
    print(num) #14
     
    num*=2
    print(num) #28
     
    num/=2
    print(num) #14
    
    num%=2
    print(num) #0
    ```
## 2.3. 숫자처리함수
1. 절댓값 (abs)
    ```python
    print(abs(-5)) #5
    print(abs(3))  #3
    ```

2. 거듭제곱 (pow)
    ```python
    print(pow(4,2))  #4^2=4*4=16
    print(pow(3,3))  #3^3=27
    ```

3. 최대값 (max)
    ```python
    print(max(5,12))    #12
    print(max(1,2,4,5)) #5
    ```

4. 최소값 (min)
    ```python
    print(min(5,12))    #5
    print(min(1,2,4,5)) #1
    ```

5. 반올림(round)
    ```python
    print(round(3.14)) #3
    print(round(4.99)) #5
    ```

6. 내림(floor, math 필수)
    ```python
    from math import *
    print(floor(4.99)) #4
    print(floor(3.24)) #3
    ```

7. 올림(ceil, math 필수)
    ```python
    from math import *
    print(ceil(3.22)) #3
    print(ceil(5.11)) #5
    ```

8. 제곱근(sprt, math 필수)
    ```python
    print(sprt(16)) #4
    print(sprt(25)) #5
    ```

## 2.4. 랜덤함수
**random 필수!**
1. random: 0.0~1.0 미만의 임의의 값을 생성한다.
    ```python
    print(random())
    
    #응용1. 0.0-10.0 미만의 임의의 값을 생성
    print(random()*10)
    
    #응용2. 0-10 미만의 임의의 정수값 생성
    print(int(random()*10))
    
    #응용3. 1-10 이하의 임의의 정수값 생성
    print(int(random()*10))+1
    ```

2. randrange: 사용자가 지정한 임의의 숫자 이상/임의의 숫자 미만의 값을 출력한다.
    ```python
    # 1이상 46미만의 임의의 값 생성
    print(randrange(1,46))
    ```

3. randint: 사용자가 지정한 임의의 숫자 이상/임의의 숫자 이하의 값 출력
    ```python
    # 1이상 45이하의 임의의 값 생성
    print(randint(1,45))
    ```

## 퀴즈#2
당신은 최근의 코딩스터디 모임을 새로 만들었다.
월 4회 스터디를 하는데 3번은 온라인/1번은 오프라인으로 하기로 하였다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하라.

조건1. 랜덤으로 날짜를 뽑는다.

조건2. 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 한다.

조건3. 매월 1~3일은 스터디 준비를 해야하므로 제외한다.

출력문 예제: 오프라인 스터디 모임 날짜는 매월 X일로 선정되었습니다.

------
해답
```python
from random import *
day=randint(4,28)
print('오프라인 스터디 모임 날짜는 매월',day,'일로 선정되었습니다')
```
