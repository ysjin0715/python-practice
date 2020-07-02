# 예외처리
## 정의
다양한 사유(접속지연, 잘못된 지정 등)로 인해 발생하는 에러를 처리하는 것.
- 아래 코드에서 텍스트 값을 입력할 경우 에러가 발생하는 것을 확인할 수 있다.
```python
print("나누기 전용 계산기입니다.")
num1 = int(input("첫 번째 숫자를 입력하시오: "))
num2 = int(input("두 번째 숫자를 입력하시오: "))
print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
```
- 에러를 잡아내기 위해서는 별도의 예외처리가 필요하다.
1. except ValueError: = 잘못된 값을 입력받은 것에 대한 예외처리
2. except ZeroDivisionError: = 0으로 나누는 것으로 인하여 발생하는 에러에 대한 예외처리
3. except: = 위에서 지정하지 않았던 별도의 에러에 대한 예외처리
4. as err: = 발생한 에러에 대한 정보를 담는 그릇

```python
try:
   print("나누기 전용 계산기입니다.")
   nums = []
   nums.append(int(input("첫 번째 숫자를 입력하시오: ")))
   nums.append(int(input("두 번째 숫자를 입력하시오: ")))
# 출력한 값을 리스트에 추가하는 코드는 삽입하지 않는다. (리스트 범위 밖의 값을 출력하라는 코드가
# 아래 존재하므로 에러가 발생할 수 있다)
   print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2])))

except ValueError as err:
   print("에러! 잘못된 값을 입력하였습니다.")
# num값에 숫자가 아닌 텍스트를 입력할 경우 print 내의 문장을 출력한다.

except ZeroDivisionError as err:
   print(err)
# num값에 0을 넣을 경우 division by zero의 값을 출력한다.

except Exception as err:
   print("알 수 없는 에러가 발생하였습니다")
   print(err)
# 위의 에러 외 다른 사유로 인해 발생하는 에러는 print안의 값을 출력한다.
```

## 의도적인 에러 발생
- raise : 일정한 조건에 맞아떨어진다면 지정된 에러를 발생시킨다.
```python
try:
   print('한 자리 숫자 나누기 전용 계산기.')
   num1 = int(input('첫 번째 숫자 입력'))
   num2 = int(input('두 번째 숫자 입력'))
   if num1 >= 10 or num2 >= 10:
      raise ValueError
# num1 혹은 num2에서 10 이상의 수를 입력하면 ValueError를 발생시킨다 

   print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
   print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')
# ValueError가 발생한다면 except ValueError:로 넘어와 print 내 값을 출력한다.
```

## 사용자 지정 에러 발생
- 별도의 class를 만들어 에러를 만들어낼 수도 있다.
```python
class BigNumberError(Exception):
   def __init__(self, msg):
      self.msg = msg

   def __str__(self):
      return self.msg

try:
   print('한 자리 숫자 나누기 전용 계산기.')
   num1 = int(input('첫 번째 숫자 입력'))
   num2 = int(input('두 번째 숫자 입력'))
   if num1 >= 10 or num2 >= 10:
      raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
# 조건문에 부합하면 BigNumberError를 출력한다.

   print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError:
   print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')

except BigNumberError as err:
   print('에러가 발생하였습니다. 한 자리 숫자만 입력하세요.')
   print(err)

# BigNumberError가 출력되면 except BigNumberError as err: 아래 값을 모두 출력한다.
# err에 담겨진 BigNumberError의 메세지를 출력한다.
```

## finally
- finally : 코드에 문제가 생기던지, 혹은 정상적으로 작동하던지 상관없이 finally 아래 구문을 출력한다.

```python
class BigNumberError(Exception):
   def __init__(self, msg):
      self.msg = msg

   def __str__(self):
      return self.msg

try:
   print('한 자리 숫자 나누기 전용 계산기.')
   num1 = int(input('첫 번째 숫자 입력'))
   num2 = int(input('두 번째 숫자 입력'))
   if num1 >= 10 or num2 >= 10:
      raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
   print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError:
   print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')

except BigNumberError as err:
   print('에러가 발생하였습니다. 한 자리 숫자만 입력하세요.')
   print(err)

finally:
   print('계산기를 이용해주셔서 감사합니다.')
# 어떠한 오류가 발생하더라도 finally 아래 값은 모두 출력된다.
```

## 퀴즈
조건1. 1보다 작거나 숫자가 아닌 입력갑싱 들어올 때는 ValueError로 처리한다.
출력메세지 : "잘못된 값을 입력하셨습니다."

조건2. 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정한다.
치킨 소진 시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램 종료
출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다"

- 내가 쓴 답
```python
class SoldOutError(Exception):
   def __init__(self,msg):
      self.msg = msg

chicken = 10
waiting = 1
try:
   while(True):
      print('[남은 치킨 : {0}]'.format(chicken))
      order = int(input('치킨 몇 마리 주문하시겠습니까? '))

      if order < 1:
         raise ValueError

      if order > chicken:
         print('재고가 부족합니다.')

      else:
         print('대기번호 {0}] {1} 마리 주문이 완료되었습니다.'.format(waiting, order))
         waiting += 1
         chicken -= order

         if chicken <= 0:
            raise SoldOutError('재고가 소진되어 더 이상 주문을 받지 않습니다.')

except SoldOutError as err:
   print(err)

except ValueError as err:
   print('잘못된 값을 입력하셨습니다')
```

- 정답
```python
class SoldOutError(Exception):
   pass

chicken = 10
waiting = 1
while(True):
   try:
      print('[남은 치킨 : {0}]'.format(chicken))
      order = int(input('치킨 몇 마리 주문하시겠습니까? '))
      if order > chicken:  # 남은 치킨보다 주문량이 많을 때
         print('재고가 부족합니다.')
      elif order <= 0:  # 주문한 치킨량이 0 이하일 때
         raise ValueError

      else:
         print('대기번호 {0}] {1} 마리 주문이 완료되었습니다.'.format(waiting, order))
         waiting += 1
         chicken -= order

      if chicken <= 0:
         raise SoldOutError

   except ValueError:
      print('잘못된 값을 입력하셨습니다')
   except SoldOutError:
      print('재고가 소진되어 더 이상 주문을 받지 않습니다.')
      break
```