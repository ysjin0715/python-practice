# 모듈과 패키지
## 모듈
- 코드의 재사용 등 편의에 의하여 코드를 하나의 부품화시키는 과정.
- 파이썬의 코드를 담고 있는 파일 (.py)
- 다른 파일에 저장된 모듈도 사용가능하다.
1. 다른 파일에 저장된 모듈을 사용하기 위해서는 해당 모듈이 저장된 파일과 사용하고자 하는 장소의 파일이 같은 폴더 내 위치해야 한다.
2. 파이썬 라이브러리에 모여있는 폴더/파일 내 위치해야 한다.
- import (모듈이 담긴 파일명)
- import (모듈이 담긴 파일명) as (파일명을 대체할 별칭)
- from (모듈이 담긴 파일명) import *
- from (모듈이 담긴 파일명) import (모듈명1), (모듈명2)...
- from (모듈이 담긴 파일명) import (모듈명1) as (모듈의 별칭)

```python
# 사람 수에 따라서 가격을 알 수 있는 모듈
# 일반 가격 환산
def price(people):
   print("{0}명 가격은 {1}원 입니다.".format(people, people*10000))

# 조조할인 가격
def price_morning(people):
   print("{0}명 조조할인 가격은 {1}원 입니다.".format(people, people*6000))

# 군인할인 가격
def price_soldier(people):
   print("{0}명 군인할인 가격은 {1}원 입니다.".format(people, people*4000))

# import Memo (다른 파일에서 모듈을 끌어와 사용할 경우, import 뒤에 파일명을 입력한다. (.py를 생략한다)
# Memo.price(3)
# Memo.price_morning(4)
# Memo.price_soldier(5)

# import Memo as mv (사용하고자 하는 모듈에 별명을 붙여 (as 뒤의 이름) Memo라는 모듈명을 대체하여 사용하도록 한다)
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from Memo import * (사용하고자 하는 모듈을 별도의 지정없이 사용할 때 사용)
# price(3)
# price_morning(4)
# price_soldier(5)

# from Memo imoprt price, price_morning (원하는 모듈만 사용하고자 할 경우, from 뒤에 모듈명을 적어야 한다)
# price(5)
# price_morning(4)
# price_soldier(3)  # 정의되지 않은 함수라고 출력되며 오류가 발생한다.

# from Memo import price_soldier as price (단축된 별명으로 군인할인의 정보를 알고 싶을 때 사용)
# price(5) = 5명 군인할인 가격은 20000원입니다.
```

## 패키지
- 모듈을 모은 컬렉션으로, import, 혹은 from import 구문으로 활용한다.
1. import (모듈이 담긴 파일이 속한 폴더).(모듈이 담긴 파일명) - import 구문에서는 모듈 및 패키지만 활용가능하다.
2. from (모듈이 담긴 파일이 속한 폴더).(모듈이 담긴 파일명) import (모듈명)- from import 구문에서는 모듈, 패키지 및 클래서 모두 활용가능하다.
3. from (모듈이 담긴 파일ㅇ 속한 폴더) import (모듈이 담긴 파일명)
```python
# Memo.py에서 입력
class VietnamPackage:
   def detail(self):
      print("[베트남 패키지 3박 5일] 다낭 효도 여행 60만원")

# Memo2.py에서 입력
class ThailandPackage:
   def detail(self):
      print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

# Memo3.py에서 입력
import lecture.Memo2  # import 구문에서는 모듈 및 패키지만 삽입이 가능하다. (클래스는 불가하다)
trip_to = lecture.Memo2.ThailandPackage()
trip_to.detail() # Memo2에 완성된 모듈을 끌어와 사용하는 것을 볼 수 있다.

from lecture.Memo2 import ThailandPackage # from import 구문에서는 모듈, 패키지 및 클래스 모두 사용가능하다.
trip_to2 = ThailandPackage()
trip_to2.detail()

from lecture import Memo
trip_to3 = Memo.VietnamPackage()
trip_to3.detail()
```

##__all__
1. from (모듈이 담긴 파일이 속한 폴더명) import *을 입력할 경우, 원래는 오류가 뜨며 코드가 실행되지 않는다.
2. 그러나 __init__폴더 내에 __all__ = [("허용할 모듈의 파일명")]을 입력할 경우, __all__에 적힌 모듈만은 한시적으로 사용이 가능하다.

```python
# Memo2.py에서 입력
class ThailandPackage:
   def detail(self):
      print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

#__init__.py에서 입력
__all__ = ["Memo2"]

from lecture import *
trip_to = Memo2.ThailandPackage()
trip_to.detail()
# 올바르게 Memo2의 값이 적용되는 것을 볼 수 있다.
```

## 모듈의 직접 실행
- 모듈이 작성된 곳에서 직접 실행되는지, 아닌지 여부를 알기 위하셔 __name__ == "__main__"을 사용한다.
- 모듈이 있는 파일에서 바로 실행될 경우, __main__의 값을 갖는다.
- 모듈이 있는 곳이 아닌 다른 곳에서 실행될 경우, (모듈을 가진 파일이 속한 폴더).(모듈을 가진 파일명)의 형태를 띈다.

```python
# Memo2에서 작성
class ThailandPackage:
   def detail(self):
      print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__":
   print("Thailand 모듈을 직접 실행")
   print("이 문장은 모듈을 직접 실행할 때만 실행되요")
   trip_to = ThailandPackage()
   trip_to.detail()
else:
   print("Thailand 외부에서 모듈 호출")

# ThailandPackage 내 print문이 출력됨과 동시에 "Thailand 모듈을 직접 실행/이 문장은 모듈을 직접 실행할 때만 실행되요"라고 출력된다.

#Memo3에서 작성
from lecture import Memo2
trip_to1 = Memo2.ThailandPackage()
trip_to1.detail()

# ThailandPackage 내 print문이 출력됨과 동시에 "Thailand 외부에서 모듈 호출"이라는 문장이 출력된다.
```

## 패키지, 모듈의 위치
- 패키지, 모듈의 위치를 파악하기 위해서는 inspect함수를 import하여 사용한다.
- print(inspect.getfile(알고자 하는 함수의 이름))
```python
import inspect
import random
from lecture import Memo2
print(inspect.getfile(random)) # random함수가 저장된 위치를 출력한다.
print(inspect.getfile(Memo2))  # Memo2함수가 저장된 위치를 출력한다.
```

## pip install
- 타인이 만든 모듈을 활용할 수 있도록 모듈을 설치한다.
1. "pypi.org" 에서 필요한 코드를 탐색한다.
2. 원하는 코드를 찾으면 검색창 근처 "pip install (원하는 코드이름)"을 복사한다.
3. terminal에 해당 내용을 붙여넣기하여 설치한다.
- terminal에 "pip list"을 입력하면 설치된 패키지를 확인할 수 있다.
- terminal에 "pip show (모듈명)"을 입력하면 설치된 패키지의 속성을 확인할 수 있다.
- 업그레이드가 필요할 경우, "pip install --upgrade (업그레이드하고자 하는 모듈명)"을 terminal에 입력함으로써 설치할 수 있다.
- 삭제를 원할 경우, "pip uninstall (삭제하고자 하는 모듈명)"을 terminal 에 입력함으로써 시행할 수 있다.

## 내장함수
- 파이썬 내에 이미 내장되어 있는 함수
1. input : 사용자 입력을 받는 함수
```python
language = input("무슨 언어를 좋아하세요?")
print(language)
```
2. dir : 임의의 대상에 대하여 어떤 함수와 변수 등을 사용가능한지 표시해주는 함수 
```python
print(dir())
import random
print(dir())
import pickle
print(dir())
# 현재 사용할 수 있는 함수를 표시해준다 (import한 함수도 포함하여 표시한다)

print(dir(random))
# random 내 어떤 함수와 변수를 사용가능한지 표시한다.

1st = [1, 2, 3]
print(dir(1st))
# 현재 사용할 수 있는 함수와 더불어 리스트에 적용할 수 있는 함수까지 포괄적으로 보여준다.

name = "seung"
print(dir(name))
# 현재 사용할 수 있는 함수와 더불어 일반 string값에서 사용할 수 있는 함수까지 포괄적으로 보여준다.
```

3. 기타 내장함수는 구글에서 "list of python builtins"을 검색한다.


## 외장함수
- 구글에서 "list of python modules"를 검색하여 확인한다.
1. glob : 경로 내 폴더 / 파일 목록을 조회 (윈도우 dir)
```python
import glob
print(glob.glob("*.py"))  # 확장자가 py인 모든 파일을 검색한다.
```

2. os : 운영체제에서 제공하는 기본기능을 구현
```python
import os
print(os.getcwd())  # 현재 디렉토리 표시
folder = "semple_dir"

if os.path.exists(folder):
   print("이미 존재하는 폴더입니다.")
   os.rmdir(folder)      # 폴더삭제
   print(folder, "폴더를 삭제하였습니다.")
   
else:
   os.makedirs(folder)   # 폴더생성
   print(folder, "폴더를 생성하였습니다.")

print(os.listdir())      # lecture(현재 있는 폴더위치)에 존재하는 모든 파일 검색  
```

3. time/datetime : 시간 관련 함수 제공
```python
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 년, 월, 일, 시, 분, 초 표시

import datetime
print("오늘 날짜는 ", datetime.date.today()) # datetime 내 오늘 날짜 표시기능 존재
today = datetime.date.today()       # 오늘 날짜 저장
td = datetime.timedelta(days=100)   # 100일 저장 (timedelta : 두 날짜 사이의 간격)
print("우리가 만난지 100일은", today + td)  # 오늘부터 100일 후 날짜 출력
```

## 퀴즈 10
- 프로젝트 내에서 나만의 시그니처를 남기는 모듈을 만드시오
- 조건 : 모듈 파일명은  byme.py로 작성한다.
- 내가 쓴 답
```python
# byme.py에서 작성
class sign():
   def detail(self):
      print("이 프로그램은 나도코딩에 의해 만들어졌습니다.")
      print("유튜브 : http://youtube.com")
      print("이메일 : nadocoding@gmail.com")

# Memo.py에서 작성
import lecture.byme
a = lecture.byme.sign()
a.detail()
```

- 정답
```python
# byme.py에서 작성
def sign():
   print("이 프로그램은 나도코딩에 의해 만들어졌습니다.")
   print("유튜브 : http://youtube.com")
   print("이메일 : nadocoding@gmail.com")

# Memo.py에서 작성
import byme
byme.sign()
```