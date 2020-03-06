# 함수
## 함수란?
1. 일정한 처리코드를 담는 박스
2. def '변수'():로 표시한다.
3. def 앞 변수를 이용하여 함수를 직접 호출하지 않는 한 함수 내 코드는 실행되지 않는다.

    ```python
   def open_account():
       print('새로운 계좌가 생성되었습니다')
   
   open_account()      # 새로운 계좌가 생성되었습니다.
    ```
   
## 전달값과 반환값
1. def '변수'('전달값'): 순으로 입력한다.
2. 전달값은 함수 내에서 '이용하고자 하는 변수'를 적는다.
2. 반환값을 이용하기 위해서는 return을 이용한다.
3. 함수 내 변수의 값을 변화시켜 이를 반환함으로써 함수 밖에서도 해당 변화가 적용될 수 있도록 돕는다.
4. ,로 구분하여 여러개의 값을 한번에 반환할 수 있다. 다만 반환된 값은 튜플형식이다.

    ```python
   def deposit(balance, money): #입금값
       print('입금이 완료되었습니다. 잔액은 {0}원입니다.'.format(balance+money))
       return balance + money          # 반환값 입력
   
   def withdraw(balance, money) #출금값
       if balance >= money:
           print('출금이 완료되었습니다. 잔액은 {0}원입니다.'.format(balance-money))
           return balance - money
       else:
           print('출금이 완료되지 않았습니다. 잔액은 {0}원입니다.'.format(balance))
           return balance
   
   def night(balance, money):
       commission = 100
       return commission, balance - money - commission
      
   balance = 0                         # 최초 변수값
   balance = deposit(balance, 1000)    # deposit함수 출력//deposit 함수의 balance(0)과 money(1000)가 대입되어 반환값을 balance변수로 대입한다.
                                       # 1. deposit함수에서 적용된 balance(0)+return(1000)의 값이 반환되어
                                       # 2. deposit(0,1000)함수 호출 시 결과값으로 출력되며
                                       # 3. 이를 balance변수에 저장한다.
                                       # 출력결과 : 입금이 완료되었습니다. 잔액은 1000원입니다.
   
   print(balance)                      # 따라서 1000이 출력된다.
   
   balance = withdraw(balance, 2000)   # 출금이 완료되지 않았습니다. 잔액은 1000원입니다.
   balance = withdraw(balance, 500)    # 1. withdraw함수에서 적용된 balance(1000)-return(500)의 값이
                                       # 2. withdraw(balance, 500) 호출 시 결과값으로 출력되며
                                       # 3. 이를 balance변수에 저장한다.
                                       # 출력결과 : 출금이 완료되었습니다. 잔액은 500원입니다.
   
   print(balance)                      # 1000-500의 값이 balance내 새로 저장되었으므로 500이 출력된다.

 
   commission, balance = night (balance, 200)
   print('수수료는 {0}원이며, 잔액은 {1}원입니다.'.format(commission, balance))
   # 출력결과 : 수수료는 100원이며, 잔액은 200원입니다.
    ```
   
## 기본값
1. 함수에서 사용되는 매개변수를 지정할 때 기본값을 설정하여, 추후 함수 호출 시 해당 변수가 없으면 저장된 기본값을 호출한다.
2. def '함수명'(매개변수1='매개변수가 없을 시 호출되는 기본값'...):

    ```python
    def profile(n, a, m):
        print('이름: {0}, 나이: {1}, 언어: {2}.' format(n,a,m)
   
    profile('유재석', 20, '파이썬')        # 이름: 유재석, 나이: 20, 언어: 파이썬
    profile('김태호', 23, '자바')          # 이름: 김태호, 나이: 23, 언어: 자바
   
    def profile_a(name, age=17, main_lang='파이썬')
        print('이름: {0}, 나이: {1}, 언어: {2}.' format(name, age, main_lang)
    
    profile_a('유재석')                    # 별도로 age와 main_lang을 지정하지 않을 경우, 함수 내에서 지정된 언어를 기본값으로 하여 출력한다.
                                           # 이름: 유재석, 나이: 17, 언어: 파이썬
    profile_a('김태호')                    # 이름: 김태호, 나이: 17, 언어: 파이썬                                                         
   ```


## 키워드값
1. 함수 호출 시 '저장된 매개변수의 이름 = 원하는 값'을 적어 출력할 수 있다.
2. 키워드값을 이용하여 함수를 호출하면 함수 내 출력하고자 하는 매개변수의 위치가 바뀌더라도 올바르게 출력이 가능하다.

    ```python
    def profile(n, a, m):
         print(n, a, m)
         
    profile(n='유재석', m='파이썬', a = 20)          # 출력해야 할 매개변수값의 위치가 달라졌음에도 키워드로 지정했기에 올바르게 출력된다.
                                                    # 유재석 20 파이썬
      ```
   

## 가변인자
1. 매개변수 내 값이 몇 개가 들어갈지 예측할 수 없는 상태에서 사용가능하다.
2. def '함수명'('*매개변수'): 형태로 사용한다.
3. 가변인자를 사용하면 매개변수 내 값이 가변적이어도 출력가능하다.

    ```python
   def profile(name, age, *lang):
       print('이름: {0}, 나이: {1}'.format(name, age))
       for l in lang:                      # 여러 개 입력된 가변인자 내 값을 하나씩 대입한다.
           print(l, end=" ")               # l에 대입된 값을 하나씩 출력한다.
           print()                         # 한 줄 띄어준다.
   
   
   # 함수에 저장된 name과 age는 profile 첫번째, 두번재 값과 대응하여 들어가는 것을 확인할 수 있으나
   # age변수의 값 이후는 전부 *lang으로 들어가는 걸 확인할 수 있다.
   # *lang값의 개수가 다르나 모두 저장이 되는 것을 확인할 수 있다.
   
   profile('유재석', 20, 'python', 'java', 'C', 'C++', 'C#')
   # 출력결과 : 이름: 유재석, 나이: 20, python java C C++ C#
   
   profile('김태호', 21, 'python', 'java')
   # 출력결과 : 이름: 김태호, 나이: 21, python java
       
    ```
   

## 지역변수와 전역변수
1. 지역변수 : 함수가 호출될 때 만들어지며 함수 호출이 끝나면 사라진다.
2. 전역변수 : 프로그램 내 어디에서든 사용가능한 변수이다.

   ```python
   gun = 10
   def checkpoint(sol):
       gun = 20
       gun = gun - sol
       print('[함수 내] 남은 총 : {0}'.format(gun))
   
   print('전체 총 : {0}'.format(gun))        # 전체 총 : 10
                                             # 함수 밖 gun의 값을 받아온다. (전역변수)
   checkpoint(2)                             # 남은 총 : 18
                                             # 함수 내 gun의 값을 받아서 계산된다 (지역변수)
   print('남은 총 : {0}'.format(gun))        # 전체 총 : 10
                                             # 함수 밖 gun의 값을 받아오므로 값은 변하지 않는다. (전역변수)
    ```
 
 3. 함수 내에서 전역변수를 사용하기 위해서는 global이라는 함수를 사용한다.
 4. 전역변수가 많으면 관리하기가 힘들어지므로 권장하지는 않는다. 
   ```python
   gun = 10
   def checkpoint(sol):
       global gun                           # 전역공간에 있는 gun을 사용한다.
       gun = gun - sol
       print('[함수 내] 남은 총 : {0}'.format(gun))
   
   print('전체 총 : {0}'.format(gun))        # 전체 총 : 10
                                             # 함수 밖 gun의 값을 받아온다.
   checkpoint(2)                             # 남은 총 : 8
                                             # global함수를 통해 함수 밖 gun의 값을 받아서 계산된다
   print('남은 총 : {0}'.format(gun))        # 남은 총 : 8
                                             # 함수 내에서 전역변수를 이용했으므로 전역변수 gun의 값이 바뀐다.
   ```

5. 실무에서는 전역변수를 사용하기보다 반환값을 주로 사용한다.
    ```python
   gun = 10
   def check(gun, sol):
       gun = gun - sol
       print('[함수 내] 남은 총 : {0}'.format(gun))
       return gun
   
   print('전체 총 : {0}'.format(gun))             # 전체 총 : 10
      
   gun = check(gun,2)                             # [함수 내] 남은 총 : 8
   
   print('남은 총 : {0}'.format(gun))             # 남은 총 : 8
    ```
   
   
## 퀴즈#6
표준 체중을 구하는 프로그램을 작성하시오

성별에 따른 공식

남자: 키(m) x 키(m) x 22

여자: 키(m) x 키(m) x 21

조건1. 표준체중은 별도의 함수 내에서 계산

함수명: std_weight / 전달값: 키(height), 성별(gender)

조건2. 표준 체중은 소수점 둘째자리까지 표시

(출력예제) : 키 175cm 남자 표준 체중은 67.38kg입니다.


1. 내가 쓴 답
   ```python
   def std_weight(gender, height):
      float(height)
      height = height/100
   
      if gender == '남자':
         weight = height*height*22
         return round(weight,2)
   
      else:
         weight = height*height*21
         return round(weight,2)

   gender = input('당신의 성별을 입력하십시오: ')
   height = int(input('키를 입력하십시오: '))
   weight = std_weight(gender, height)
   print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(height, gender, weight))
   ```
   
   
2. 정답
    ```python
   def std_weight(height, gender):
       if gender == '남자':
           return height * height * 22
       
       else:
           return height * height * 21
   
   
   
   height = 175
   gender = '남자'
   weight = round(std_weight(height / 100, gender), 2)
   print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(height, gender, weight))
 
    ```