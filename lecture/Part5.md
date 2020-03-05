# 제어문
## if문에서 사용되는 함수들
1. if '조건':
    ```python
   # if에서 제시한 조건과 맞아떨어지면 if 아래 코드가 실행된다.
    weather = '비'
    if weather == '비':
       print('우산을 챙기세요')   # 우산을 챙기세요
   
   # if에서 제시한 조건과 맞지 않으면 if 아래 코드는 실행되지 않는다.
    weather = '맑음'
    if weater == '비':
       print('우산을 챙기세요')   # ''
    ```
   
 2. elif '조건' :
   ```python
    # if에서 제시한 조건과 맞지 않으면 if문에 소속되지 않은 다음 코드를 실행한다.
    # 들여쓰기의 정도로 if문에 포함되어 있는지의 여부를 알 수 있다.
    weather = '미세먼지'
    if weather == '비':
       print('우산을 챙기세요')        # if에서 제시한 조건과 맞지 않으므로 해당 코드는 실행되지 않는다.
    elif weather == '미세먼지'
       print('마스크를 챙기세요')      # elif에서 제시한 조건과 맞으므로 해당 코드가 실행된다.
    
    #출력결과: 마스크를 챙기세요
   ```

3. else:
    ```python
    #if/elif에서 제시한 조건이 맞지 않으면 else에 포함된 코드가 실행된다.
 
   weather = '맑음'
    if weather == '비':
       print('우산을 챙기세요')        # if에서 제시한 조건과 맞지 않으므로 해당 코드는 실행되지 않는다.
    elif weather == '미세먼지'
       print('마스크를 챙기세요')      # elif에서 제시한 조건과 맞지 않으므로 해당 코드는 실행되지 않는다.
    else:
       print('준비물 필요없어요')      # if/elif에서 제시한 조건이 둘다 맞지 않으므로 else문 아래 코드가 실행된다.

    #출력결과: 준비물 필요없어요
    ```

4. input('A문장')
    ```python
    # 사용자의 입력을 받아서 값을 가질 수 있도록 만드는 함수이다.
    # input으로 받는 모든 함수는 str의 값을 가지므로 수가 필요할 경우 반드시 int/float함수로 변환한다.
   
    weather = input('오늘 날씨는 어때요?')
    
   if weather == '비':
       print('우산을 챙기세요')        # if에서 제시한 조건과 맞지 않으므로 해당 코드는 실행되지 않는다.
    elif weather == '미세먼지'
       print('마스크를 챙기세요')      # elif에서 제시한 조건과 맞지 않으므로 해당 코드는 실행되지 않는다.
    else:
       print('준비물 필요없어요')      # if/elif에서 제시한 조건이 둘다 맞지 않으므로 else문 아래 코드가 실행된다.

   # 출력결과  
   #1. input 내 '오늘 날씨는 어때요?'라는 문장이 먼저 출력된 후 입력을 기다린다.
   #2. 사용자가 입력하는 값에 따라 if/elif/else 내 코드를 실행시킨다.
    ```
   
5. or
    ```python
   # if/elif 조건 내 하나의 조건을 더 추가시킨다.
   # if A or B: 라는 조건문을 입력할 때 프로그램은 A나 B 둘 중 하나의 조건만 True더라도 if문에 속한 코드를 실행시킨다.
   
   weather = "눈"
   
   if weather == "비" or weater == "눈":
       print('우산을 챙기세요')           #weather의 값이 '눈'이므로 B조건에 부합하기에 if문 아래 속한 코드가 실행된다.
   else:
       print('준비물 필요없어요')
   
   #출력결과 : 우산을 챙기세요
    ```
   
6. and
    ```python
   #if A and B라고 할때, if내 조건문을 실행시키기 위해서는 A와 B조건 모두를 충족하는 값이 들어와야 한다.
   
   # input으로 받는 모든 값은 str속성을 지니므로 int로 변환한다.
   temp = int(input('기온은 어때요?'))
   
   if 30 <= temp:
       print('너무 더워요, 나가지 마요')    # 20을 입력할 경우, if 내 조건에는 맞지 않으므로 elif의 조건을 탐색한다.
   elif 10 <= temp and temp <30:
       print('괜찮은 날씨네요')            # 20은 10 이상/30 미만의 조건을 모두 총족하므로 elif내 코드가 실행된다.
   else:
       print('너무 추워요')
   
   # 만일 20이라는 값이 입력될 경우 출력결과 : 괜찮은 날씨네요 
    ```
   
## 반복문 For
1. 단순반복에 속하는 코드를 축약하여 표현한다.
2. for '변수' in '조건' 순으로 입력한다.
3. 조건의 한도 내에서 반복을 진행한다.
    ```python
    # 방법 1
    print('대기번호 : 0')
   print('대기번호 : 1')
   print('대기번호 : 2')
   print('대기번호 : 3')
   print('대기번호 : 4')
   # 출력결과 : 대기번호 : 0....대기번호 : 4
   
   # For문을 사용한 방법2
   # [0,1,2,3,4] 내 리스트에 포함된 값을 차례대로 하나씩 watting_num에 넣어
   # for문 아래 코드에 대입한다.
   for watting_num in [0,1,2,3,4](=range(5)):
       print('대기번호 : {0}'.format(watting_num))
   #출력결과 : 대기번호 : 0....대기번호 : 4
    ```


## 반복문 while
1. while '조건'으로 입력한다.
2. 조건이 맞을 때까지 무한히 반복한다.
    ```python
    customer = '토르'
    index = 5
    while index >= 1:
      print('{0}, 커피가 준비되었습니다. {1}번 남았어요.'.format(customer, index))
      index -= 1                               # index가 0이 될 때가지 print문을 출력한다.
      if index == 0:
         print('커피는 폐기처분되었습니다.')    # index가 while문을 돌며 0이 되면 if문 내 코드를 실행한다.
            
    # 출력 결과
   # 토르, 커피가 준비되었습니다. 5번 남았어요.
   # 토르, 커피가 준비되었습니다. 4번 남았어요.
   # 토르, 커피가 준비되었습니다. 3번 남았어요.
   # 토르, 커피가 준비되었습니다. 2번 남았어요.
   # 토르, 커피가 준비되었습니다. 1번 남았어요.
   # 커피는 폐기처분되었습니다.
   ```
   
3. 무한루프문 (while True)
    ```python
   while True:
       print('토르, 커피가 준비되었습니다.')
   
   # 출력 결과 : '토르, 커피가 준비되었습니다.'라는 문장을 무한히 반복한다.
    ```

## countinue/break
1. continue: 만일 조건문이 부합할 경우, 밑의 코드를 실행시키지 않고 다음으로 넘어가도록 하는 역할을 한다.
2. break : 만일 조건문이 부합할 경우, 밑의 코드를 실행시키지 않고 반복문을 끝낸다.

```python
absent = [2, 4]
no_book = [5]
for student in range(1,7)       # 1,2,3,4,5,6
    if student in absent:       
        continue                # 2,4번은 absent 변수에 포함되어 있으므로 아래 코드를 실행시키지 않은 채 다음 번호로 넘어간다.
    elif student in no_book:
        print('오늘 수업 여기까지. {0}는 교무실로 따라와'.format(student)) # 5번은 no_book 변수 내에 포함되어 있으므로 아래 코드를 실행시키지 않고 반복문을 끝낸다.
        break
    print('{0}, 책을 읽어봐'.format(student))
# 그 외 1,3번은 print 내 함수를 출력한다.
# 5번에서 반복문이 끝나므로 6번은 실행되지 못한다.
```

## 한줄 for
```python
# ex1) 출석번호가 1,2,3,4 앞에 100을 더하기로 하였다.
student = [1,2,3,4,5]
print(student)

# b=[1,2,3,4]
# n+1 for n in b                        # b리스트 내 개체를 n에 대입하여 n+1을 수행한다.
student = [i+100 for i in student]      # student 리스트 내 개체를 i에 하나씩 대입하여 i+100을 출력한다.
print(student)                          # [101, 102, 103, 104, 105]


# ex2) 학생 이름을 길이로 변환
students = ["iron man", 'Thor', 'I am groot']
students = [len(i) for i in students]   # students리스트 내 개체를 i에 하나씩 대입하여 len(i)한다.
print(student)                          # [8, 4, 10]


# ex3) 학생 이름을 대문자로 변환
students = ["iron man", 'Thor', 'I am groot']
students = [i.upper() for i in students]  # students리스트 내 개체를 i에 하나씩 대입하여 i.upper()함수를 적용한다.
print(students)                           # ["IRON MAN", 'THOR', 'I AM GROOT']
```

## 퀴즈5
당신은 COCOA서비스를 이용하는 택시기사이다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하라

조건1. 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해진다.

조건2. 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 한다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
...
[O] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 명

1. 내가 쓴 답
    ```python
    from random import *
    count = 0
    for a in range(1,51):
       time = randrange(5,51)
       if time >= 5 and time <=15:
           print('[O]',end=" ")
           count+=1
       else:
           print('[ ]',end=" ")
       print('{0}번째 손님 (소요시간 : {1}분)'.format(a, time))

    print('총 탑승 승객 : {0}분'.format(count))
    ```
 
 2. 정답
     ```python
    from random import *
    
    cnt = 0  # 총 탑승승객 수
    for i in range(1, 51):  # 1 ~ 50 이라는 수(승객)
        time = randrange(5, 51)  # 5 ~ 50분 소요 시간
        if 5 <= time <= 15:  # 5 ~ 15분 이내의 손님(매칭 성공), 탑승 수 증가 처리
            print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
            cnt += 1
        else:  # 매칭이 실패한 경우
            print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
    
    print('총 탑승 승객 : {0} 분'.format(cnt))
    ```