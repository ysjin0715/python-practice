# 4. 자료구조
## 1. 리스트
1. 순서를 가진 객체의 나열
2. 리스트에는 다양한 자료형들을 섞어서 사용할 수 있다.
    ```python
   # subway1=10 
   # subway2=20 
   # subway3=30 
   subway=[10,20,30]
   subway=["유재석","조세호","박명수"]
   subway=['우재석',20,True]
    ```
   
   
### 리스트에서 사용하는 함수
1. 원하는 장소 출력하기(.index('찾고자 하는 내용'))
    ```python
    subway=['유재석','조세호','박명수']
   #조세호씨는 몇번째에 위치해있는가.
   #리스트는 0번째부터 시작함을 유의!
   print(subway.index('조세호'))  # 1
    ```

2. 객체를 리스트 뒤에 붙이기! (.append('추가하고자 하는 내용'))
    ```python
   subway=['유재석','조헤소','박명수']
   subway.append('하하')
   print(subway)  #['유재석','조헤소','박명수','하하']
    ```   

3. 객체를 원하는 위치에 삽입하기 (.insert(추가시키고 싶은 자리의 순번,'추가하고자 하는 내용')
    ```python
   subway=['유재석','조헤소','박명수']
   subway.insert(1,'정형돈')
   print(subway)  #['유재석','정형돈','조헤소','박명수']
   # 1번째 자리에 '정형돈'이라는 객체가 들어가고 나머지 내용은 한 칸씩 뒤로 밀린다.
    ```

4. 리스트 내 객체를 뒤에서부터 하나씩 꺼내기 (.pop())
     ```python
   subway=['유재석','조헤소','박명수']
   print(subway.pop()) # 박명수
   print(subway)       # ['유재석','조헤소']   
   print(subway.pop()) # 조헤소
   print(subway)       # ['유재석']
    ```

5. 리스트 내 같은 내용이 몇 개가 들어있는가(.count('찾고자 하는 내용'))
   ```python
   subway=['유재석','유재석','박명수','유재석']
   print(subway.count('유재석'))  # 3
    ```
   
6. 리스트 내용을 정렬하기 (.sort())
    ```python
   # sort를 사용하면 변수에 리스트 내용이 정렬된 채 저장됨을 인지하자! 
   num_list=[1,5,4,2,3]
   num_list.sort()
   print(num_list)  #[1,2,3,4,5]
    ```
   
7. 리스트 내용을 정렬하기2 (sorted('리스트 변수'))
    ```python 
   num_list=[1,5,4,2,3]
   number = sorted(num_list) 
   #sorted 함수가 num_list의 값에 영향을 주지 않았다!
   print(num_list)  #[1,5,4,2,3]
   print(number)    #[1,2,3,4,5]
    ```
 
7. 리스트 내용을 뒤집어 정렬하기 (.reverse())
    ```python
   # reverse를 사용하면 변수의 리스트 내용이 재정렬된 채로 저장됨을 유의하자!
   num_list=[1,2,3,4,5]
   num_list.reverse()
   print(num_list)  # [5,4,3,2,1]
    ```
   
8. 모두 지우기 (.clear)
    ```python
   num_list=[1,2,3,4,5]
   num_list.clear()
   # num_list 내부 모든 객체가 지워짐을 알 수 있다.
   print(num_list)  # []
    ```
   
9. 리스트를 합치기 (.extend('합치고자 하는 리스트의 변수명')
    ```python
   a=[1,2,3,4,5,6]
   b=['박명수','유재석','정형돈']
   a.extend(b)
   # a 라는 리스트에 b라는 리스트가 종속되어 합쳐지는 형태이므로 반드시 변수 호출시에는 괄호안에 들어간 변수명이 아닌 밖에 나와있는 변수명으로 호출한다. 
   print(a) # [1,2,3,4,5,6,'박명수','유재석','정형돈']
    ```
   

## 사전
1. 키/값이 하나의 쌍을 이루어 자료를 저장하는 형태
2. 키는 중복하여 지정할 수 없다.
3. 중괄호로 표시한다.
   ```python
   # '키 : 값' 형태로 배열하여 입력
   cabinet = {3:'유재석',100:'김태호'}
   ```
   
### 사전을 이용하는 방법
1. 자료를 꺼내는 방법1. 키를 입력하여 자료 호출
    ```python
   cabinet = {3:'유재석',100:'김태호'}
   print(cabinet[3])   # 유재석
   print(cabinet[100]) # 김태호
   # 단, 배정되지 않은 키로 값을 호출할 경우 오류가 발생한다.
   print(cabinet[5])   # 오류!
    ```
   
2. 자료를 꺼내는 방법2. .get(키 입력,'기본값')을 사용하여 자료 호출
    ```python
   cabinet = {3:'유재석',100:'김태호'}
   print(cabinet.get(3)) # 유재석
   # 배정되지 않은 키로 값을 호출할 경우 'None'을 출력한다.
   print(cabinet.get(5))            # None
   # 배정되지 않은 키로 값을 호출할 때 키와 '기본값'을 같이 쓰면, 'None'대신 '기본값'을 출력한다.
   print(cabinet.get(5,'사용가능'))  # 사용가능
    ```

3. 자료의 추가/변경
   ```python
   cabinet = {3:'유재석',100:'김태호'}
   cabinet[3] = '김종국'
   cabinet['A3'] = '조세호'
   
   #기존키에 배정되어 있던 '유재석'이라는 값이 빠지고 '김종국'이 추가된다.
   #A3이라는 키가 새로 배정되어 키와 값이 새로 추가된다.
   
   print(cabinet) # {3:'김종국', 100:'김태호', 'A3':'조세호'}
    ```
   
4. 자료의 삭제(del)
   ```python
   cabinet = {3:'유재석',100:'김태호'}
   
   del cabinet[3]
     
   # 3이라는 키가 삭제되면서 키와 쌍을 이루고 있던 값도 삭제된다.
   print(cabinat)  # {100: '김태호'} 
   ```

5. 해당 키가 사전 안에 있는가? ('key' in '사전')
    ```python
   cabinet = {3:'유재석',100:'김태호'}
   # 사전 내 사용자가 질문한 키가 있을 경우 True값을 반환한다.
   print(3 in cabinet)  # True
   # 사전 내 사용자가 질문한 키가 없을 경우 False값을 반환한다.
   print(5 in cabinet)  # False
   
   #숫자가 아니더라도 똑같이 출력할 수 있다.
   cabinet ={'A-3':'유재석',100:'김태호'}
   print('A-3' in cabinet) # True   
    ```
   
6. 해당 함수에서 무슨 키를 사용하고 있는가. (.keys()))
    ```python
   cabinet = {3:'유재석',100:'김태호'}
   print(cabinet.keys())  # dict_keys([3, 100])   
    ```
   
7. 해당 함수에서 무슨 값를 사용하고 있는가. (.values())
    ```python
   cabinet = {3:'유재석',100:'김태호'}
   print(cabinet.values())  # dict_values(['유재석', '김태호'])   
    ```
 
8. 키와 값을 쌍으로 출력한다. (.items())
    ```python
   cabinet = {3:'유재석',100:'김태호'}
   print(cabinet.items())  # dict_items([(3, '유재석),(100, '김태호')])   
    ```
   
9. 사전 내 모든 내용을 초기화(.clear())
    ```python
   cabinet = {3:'유재석',100:'김태호'}
   cabinet.clear()
   
   # 모든 내용이 삭제되어 껍데기만 남는다.
   print(cabinet)  # {}   
    ```   

## 튜플
**1. 리스트와는 다르게 내용변경이 불가하다.**
2. 그러나 처리속도가 리스트보다 빠르므로 '변경될 필요가 없는 내용'을 처리할 때 주로 사용한다.
3. 튜플은 괄호를 이용하여 내용을 묶는다.
    ```python
    memu = ('돈가스','치즈가스')
   
   # 내용 호출방법은 리스트와 동일하다.
   print(menu[0])      # 돈가스
   print(menu[1])      # 치즈가스
   
   
   # 튜플은 변수와 값을 한번에 선언/저장하는 게 가능하다.
   (name, age, hobby) = ('김종국',20,'코딩')
   print(name, age, hobby) # 김종국 20 코딩
    ```
   
## 집합 (set)
1. 중복이 불가능하다.
2. 순서가 없다.
3. 집합은 {}를 이용하여 선언한다/혹은  set(['집합 내 들어갈 내용들...'])을 이용하여 선언한다.
    ```python
   my_set = {1,2,3,3,3}
   my_set1 = set([1,2,3,3,3])
   
   #중복된 값은 삭제된다.
   print(my_set)   # {1,2,3}
   
   #{}로 묶었던 세트와 똑같은 값이 출력된다.
   print(my_set1)  # {1,2,3}
   ```
   
### 집합에서 사용하는 함수들
1. 교집합의 출력 (& 연산자, .intersecton('교집합을 원하는 변수'))
    ```python
   java = {'유재석','김태호','양세형'}
   python = set(['유재석','박명수'])
   
   #1. &를 이용한 교집합의 출력
   print(java & python)    # {'유재석'}
   
   #2. .intersection을 이용한 교집합의 출력
   print(java.intersection(python))    # {'유재석'}
    ```
  

2. 합집합의 출력 ( |, .union('합집합을 원하는 변수'))
    ```python
   java = {'유재석','김태호','양세형'}
   python = set(['유재석','박명수'])
   
   #1. |를 이용한 합집합의 출력
   print(java | python)        # {'김태호','박명수','유재석','양세형'}
   
   #2. .union을 이용한 합집합의 출력
   print(java.union(python))   # {'김태호','박명수','유재석','양세형'}
   
   #합집합의 순서가 뒤바뀐 이유는 집합의 경우 순서가 없기 때문이다.
    ```


3. 차집합의 출력 ( - 연산자, difference('값을 제외시키고자 하는 집합의 변수명')))
    ```python
   java = {'유재석','김태호','양세형'}
   python = set(['유재석','박명수'])
   
   #1. -를 이용한 차집합의 출력
   print(java - python)            # {'양세형', '김태호'}
   
   #2. difference를 이용한 차집합의 출력
   print(java.difference(python))  # {'양세형', '김태호'}
    ```

4. 집합 내용의 추가/삭제 (.add('추가하고자 하는 내용...')/.remove('삭제하고자 하는 내용...'))
    ```python
   java = {'유재석','김태호','양세형'}
   python = set(['유재석','박명수'])
   
   #1. 집합 내용의 추가(.add)
   python.add('김태호')
   print(python)       # {'박명수','김태호','유재석'}
   
   #2. 집합 내용의 삭제(.remove)
   java.remove('김태호')  
   print(java)         # {'유재석','양세형'}
    ```
   

## 자료구조의 변경
1. 집합 - 리스트 - 튜플 간에는 자료구조를 변경할 수 있다.
2. 사전 형태로는 바꿀 수 없다(키/값이 쌍으로 입력되어있기 때문!)
```python
#1. 집합 형태로 자료 입력
menu = {'커피','우유','주스'}
print(menu, type(menu))             # {커피, 우유, 주스} <class 'set'>

#2. 리스트 형태로 변환
menu = list(menu))
print(menu, type(menu))             # {커피, 우유, 주스} <class 'list'>

#3. 튜플 형태로 변환
menu = tuple(menu)
print(menu, type(menu))             # {커피, 우유, 주스} <class 'tuple'>

#4. 집합 형태로 변환
menu = set(menu)
print(menu, type(menu))             # {커피, 우유, 주스} <class 'set'>
```


## 퀴즈#4
당신의 학교에서는 파이썬 코딩대회를 주최한다.
참석률을 높이기 위하여 댓글 이벤트를 진행한다.
댓글 작성자들 중에 추첨을 통하여 1명은 치킨, 3명은 커피 쿠폰을 받게 된다.
추첨 프로그램을 작성하라.

조건1. 편의상 댓글은 20명이 작성하였으며, 아이디는 1~20이라고 가정

조건2. 댓글 내용과는 상관 없이 무작위로 추첨하되 중복은 불가

조건3. random 모듈의 shuffle(리스트 내 자료를 무작위로 섞는다) 와 sample(리스트 내 자료를 무작위로 뽑는다)를 사용하라


1. 출력예제
   ```python
   --당첨자 발표--
   치킨 당첨자 : 1
   커피 당첨자 : [2, 3, 4]
   --축하합니다-- 
   ```
2. 정답
    ```python
    from random import *
    # 아이디 생성
    users = range(1,21)  # 1 이상 21 미만까지 숫자를 생성
    users = list(users)
    
    # 아이디 뒤섞기
    shuffle(users)
    
    # 치킨/커피 당첨자 뽑기
    winners = sample(users, 4)
    
    print("-- 당첨자 발표 --")
    print('치킨 당첨자 : {0}'.format(winners[0]))
    print('커피 당첨자 : {0}'.format(winners[1:]))
    print('-- 축하합니다 --"')
    ```