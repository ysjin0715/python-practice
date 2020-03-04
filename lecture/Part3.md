# 3. 문자열 처리
## 문자열
1. 작은따옴표/큰따옴표 내 들어가는 모든 형태의 값

### 문자열의 사용 형태
1. 일반적인 형태
    ```python
    print('파이썬은 어려워요') #파이썬은 어려워요
    print("파이썬은 어려워요") #파이썬은 어려워요
    ```

2. 여러줄 출력
    ```python
    print("""파이썬은
    어려워요""")
    #파이썬은
    어려워요
    ```

## 슬라이싱
1. 문자열 중에서 필요한 부분만 잘라서 사용하는 것
2. 문자열은 "0번째"부터 시작하므로 슬라이싱 시 주의한다.
    ```python
    jumin=990120-1234567
    
    print("성별: "+jumin[7]) #성별: 1
    
    #한 덩어리를 가져오기 위해서는 :과 함께 인덱스를 적는다.
    #[0:2] => 0번째부터 2번째 전까지 (0~1번째 값)
    print("연: "+jumin[0:2]) #연: 99
    print("월: "+jumin[2:4]) #월: 01
    print('일: '+jumin[4:6]) #일: 20
    
    #처음부터 값을 가져오고 싶다면 앞의 0은 생략해도 좋다
    #[0:6] = [:6]
    print('생년월일: '+jumin[:6]) #생년월일: 990120
    
    #마지막부터 값을 가져오고 싶다면 뒤의 숫자를 생략한다.
    #[7:14]=[7:]
    print('뒤 7자리: '+jumin[7:]) #뒤 7자리: 1234567
    
    #거꾸로 숫자를 세어서 값을 출력하고 싶다면 음수로 값을 대입한다.
    #[7:14]=[-7:0]=[-7:]
    print('뒤 7자리 (뒤에서부터 계산해보기): '+jumin[-7:0]) #뒤 7자리 (뒤에서부터 계산해보기): 1234567
    ```

## 문자열처리함수
1. 모든 문자를 소문자로(.lowar())
    ```python
    python='Python is Amazing'
    print(python.lower())
    #python is amazing
    ```

2. 모든 문자를 대문자로(.upper())
    ```python
    python='Python is Amazing'
    print(python.upper())
    #PYTHON IS AMAZING
    ```

3. n번째 알파벳이 대문자인가(.isupper())
    ```python
    #첫번째 알파벳이 대문자인가
    python='Python is Amazing'
    print(python[0].isupper()) #True
    ```

4. 문자열의 길이반환(len)
    ```python
    python='Python is Amazing'
    print(len(python)) #17
    ```

5. 원하는 문자를 다른 문자로 바꾸기(replace(변환하고자 하는 값,변환을 희망하는 값))
    ```python
    #Python을 java로 바꾸기
    python='Python is Amazing'
    print(python.replace('Python','java')) #java is Amazing
    ```

6. 원하는 문자가 어디 있는가(index(위치를 알고자 하는 문자))
    ```python
    #만일 한 문장 내 찾고자 하는 문자가 여러개 있을 경우, 가장 앞의 값을 반환한다.
    python='Python is Amazing'
    index=python.index('n')
    print(index) #5
        
    # 앞에서 찾은 위치 다음부터 원하는 문자의 위치 찾기
    #'n'이라는 문자를 5번째 이후 어디에 위치해있는가.
    index=python.index('n',index+1)
    print(index) # 15
        
    #만일 자신이 찾고자 하는 문자가 문장 내 없을 경우 오류를 반환한다.
    index=python.index('java')
    print(index) #오류!
    ```

7. 원하는 문자가 어디 있는가.(find(찾고자 하는 문자))
    ```python
    #사용법은 index와 비슷하며 출력값도 같다.
    python='Python is Amazing'
    print(python.find('n'))  # 5
    print(python.index('n')) # 5
    
    #그러나, 자신이 찾고자 하는 문자가 문장 내 없을 경우, index와는 다르게 -1을 반환한다.
    print(python.index('java')) # 오류
    print(python.find('java'))  # -1
    ```

8. 원하는 문자는 몇개나 있지? (count(갯수를 알고자 하는 문자))
    ```python
    python='Python is Amazing'
    print(python.count('n'))  # 2
    ```


## 문자열 포맷
1. 숫자를 집어넣고싶어요!(%d)
    ```python
    #항상 정수값만 집어넣을 수 있음을 기억한다.
    print('나는 %d살입니다.'%20) #나는 20살입니다.
    print('나는 %d살이 됩니다'%10) #나는 10살이 됩니다.
    
    #여러개의 값을 넣고 싶을 경우, 두개를 사용한다.
    print('나는 %d살이고, 쟤는 %d살이다.'%(20,10)) #나는 20살이고, 쟤는 10살이다.
    ```

2. 문자열을 집어넣고싶어요!(%s)
    ```python
    #문자열을 넣을 때 사용한다.
    print('나는 %s를 좋아해요'%'사과') #나는 사과를 좋아해요
    
    #%s를 사용하면 %d나 %c를 구분할 필요 없이 모든 값들이 정상적으로 출력된다.
    print('나는 %s살입니다'%20) #나는 20살입니다.
    print('Apple은 %s로 시작한다'%"A") #Apple은 A로 시작한다.

    #여러 개를 사용하고 싶을 경우 두번 사용하면 된다.
    print('나는 %s이고, 쟤는 %s이다.'%(이름1, 이름2)) #나는 이름1이고, 쟤는 이름2이다.
    ```

3. 한글자만 집어넣고싶어요!(%c)
    ```python
    #%자리에 한 글자만 넣고 싶을때 사용한다.
    print('Apple은 %c로 시작한다'%"A") #Apple은 A로 시작한다.
    
    #여러 개를 사용하고 싶을 경우 두번 사용하면 된다.
    ```

3. format함수
    ```python
    #숫자/문자열 상관없이 사용가능하다.
    print("나는 {}살입니다.".format(20)) #나는 20살입니다.
    print("나는 {}색과 {}색을 좋아해요.".format('빨간','파란')) # 나는 빨간색과 파란색을 좋아해요.
    
    #뒤에 들어가는 글자의 순서를 바꾸고 싶다면 중괄호 내 숫자를 쓴다.
    #순서는 무조건 0번째부터 시작한다.
    print("나는 {0}색과 {1}색을 좋아해요.".format('빨간','파란')) # 나는 빨간색과 파란색을 좋아해요.
    print("나는 {1}색과 {0}색을 좋아해요.".format('빨간','파란')) # 나는 파란색과 빨간색을 좋아해요.
    
    #format 뒤에 오는 숫자/문자를 변수에 넣어서 사용할 수도 있다.
    #변수로 호출할 경우, 순번과는 상관없이 해당 변수에 대한 값이 출력된다.
    print('나는 {age}살이며, {color}색을 좋아해요'.format(color='빨강',age=20))
    
    #전역변수의 값을 그대로 받아서 사용할 수도 있다.
    #파이썬 버전 3.6v이상만 사용가능
    age=20
    color='빨강'
    print(f'나는 {age}살이며, {color}색을 좋아해요') #나는 20살이며, 빨강색을 좋아해요
    ```


## 탈출 문자
1. 문장 내 줄바꾸기(\n)
    ```python
    print('백문이 불여일견\n백견이 불여일타')
    #백문이 불여일견
    #백견이 불여일타
    ```

2. 문장 내 큰/작은따옴표 온전히 출력하기(\)
    ```python
    print("저는 \"나도코딩\"입니다") #저는 "나도코딩"입니다.
    print("저는 \'나도코딩\'입니다") #저는 '나도코딩'입니다.
    ```

3. 문장 내에서 \ 출력하기 (\\)
    ```python
    print("C:\\Users") # C:\Users
    ```
   
4. 커서를 맨 앞으로 이동하여 내용수정하기 (\r))
    ```python
    #\r부분에서 커서가 맨 앞으로 움직여 \r뒤 Pine이라는 내용을 다시 입력한다.
    print('Red Apple\rPine') #PineApple
    ```
   
5. 한 글자 삭제하기! (\b)
    ```python
    #\b부분에서 \b앞 한 글자를 삭제한 후 출력한다.
    print("Redd\bApple") # RedApple
    ```
   
6. 탭하기 (\t)
    ```python
   #\t부분에서 tab을 입력한 채로 출력한다. 
   print("Red\tApple") #Red    apple
    ```


## 퀴즈3
사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

규칙1. hhtp://부분은 제외하기
규칙2. 처음 만나는 점(.)이후 부분은 제외
규칙3. 남은 글자 중 처음 세자리+글자갯수+글자 내 'e'개수+'!'로 구성

ex) http://naver.com로 생성된 비밀번호 : nav51!

---
해답
```python
add='http://naver.com'
sec_point=int(add.find('.'))
secret1=add[7:sec_point]
result=secret1[:3]+str(len(secret1))+str(secret1.count('e'))+"!"

print(result)
```

---

<정식 해답>
```python
url='http://naver.com'
my_str=url.replace('http://',"") #규칙1 
my_str=my_str[:my_str.index(".")] #[0:5] -> 0~5직전까지, 0,1,2,3,4
password=my_str[:3]+str(len(my_str))+str(my_str.count('e'))+"!"

print("{0}의 비밀번호는 {1}입니다.".format(url,password))
```
