# 입출력
## 표준입출력
### sep=
1. 구분기호 (,)를 포함한 값을 출력할 시 구분기호를 기본값 대신 원하는 값으로 바꾸어준다.
2. 기본값은 " "(띄어쓰기)로 설정되어있다.
    ```python
   print('파이썬','어려워요',sep="/")            # 파이썬/어려워요
   print('파이썬','어려워요',sep="")             # 파이썬어려워요
    ``` 
   
### end=
1. 값을 출력할 시 해당 값의 끝부분을 기본값 대신 원하는 값으로 바꾸어준다.
2. 기본값은 줄바꿈으로 설정되어있다.
    ```python
   print('파이썬은 어려워요',end="")
   print('파이썬은 어려워요')
   # <출력결과>
   # 파이썬은 어려워요
   # 파이썬은 어려워요
    ```

### stdout / stderr
1. import sys를 먼저 선언한다.
2. 출력하고자 하는 값 끝에 file=stdout을 적으면 표준출력으로 처리한다.
3. 출력하고자 하는 값 끝에 file=stderr을 적으면 표준에러으로 처리한다.
4. 다만 콘솔에 표시되는 내용은 둘 차이가 없다.

   ```python
   from sys import *
   print('python','java',file = stdout)        # python java
   print('python','java',file = stderr)        # python java
   ```

### .ljust / .rjust
1. '출력하고자 하는 값/변수' . ljust / rjust ('공간을 확보하고자 하는 칸의 수')
2. ljust는 괄호에 적힌 수 만큼 공간을 확보한 후 '왼쪽'정렬한다.
3. rjust는 괄호에 적힌 수 만큼 공간을 확보한 후 '오른쪽 정렬한다.

   ```python
   scores = {'수학':0, '영어':50, '코딩':100}
   for subject, score in scores.items():       # scores 사전 내 키와 값을 동시에 출력하여 각각 subject, score에 대입한다.
       print(subject.ljust(8), str(score).rjust(4), sep = ":")
   # <처리과정>
   #1. 분리기호를 기준으로 8칸의 공간을 확보하고 subject 내 값을 입력하여 왼쪽정렬한다.
   #2. 분리기호를 기준으로 4칸의 공간을 확보하고 score 내 값을 입력하여 오른쪽정렬한다.
   
   # <출력결과>
   # 수학      :    0
   # 영어      :   50
   # 코딩      :  100
   ```
   
### .zfill
1. .zfill('값이 없을 때 삽입하고자 하는 0의 개수')로 입력한다.
2. 값이 있으면 해당 값이 제대로 출력되며, 나머지는 0으로 채워진다.
   ```python
   for num in range(1,21):
        print('대기번호 : '+str(num).zfill(3))
   
   # <출력결과>
   # 대기번호 : 001
   # ...
   # 대기번호 : 020
   ```

### input
1. '변수' = input('희망하는 문자를 적으면 됩니다...')
2. input 내 적혀있는 문자가 출력되며 입력을 대기한다.
3. 값을 입력하면 해당 값이 input 앞의 변수에 저장된다.
4. 저장되는 값은 무조건 문자열의 형태를 지닌다.

   ```python
   a = input('아무 말이나 할래요 : ')
   print(a)
   
   # '아무 말이나 할래요 : '라는 문자가 출력되며 입력을 대기한다.
   # 사용자가 입력하는 값이 출력된다.   
   ```
   

## 다양한 출력포맷
### {} 내에서 출력값 조정하기
1. 통상 사용방법 : "{'몇번째 글자부터 적용할 것인가(숫자로 입력) : '빈 공간은 어떻게 출력할 것인가''정렬하고자 하는 방향(<,>,^ 중에서 선택)''(양수/음수에 따라서 부호를 출력하고 싶다면 '+'를 붙여줄 것) 확보하고자 하는 글자의 포인트 수'}"
   ```python
   print("{0: >10}".format(500))       #        500
    # 오른쪽정렬
    
    print("{0: <10}".format(500))       # 500
    # 왼쪽정렬
    
    print("{0: ^+10}".format(-500))       #   -500
    # 가운데 정렬
    
    print("{0:-^5}".format(500))       #-500-
    # : 다음에 써놓은 문자에 따라 출력값이 달라진다.
   ```

2. 숫자 쉼표(구분기호) 만들기 ("{몇번째 글자부터 적용할 것인가(숫자로 입력):(양/음수를 구분하고자 한다면 여기에 '+'를 적어주세요),}")
   ```python
   print("{0:,}".format(100000000))   # 100,000,000
   
   print("{0:+,}".format(-100000000)) # -100,000,000
   ```
   
3. 1번과 2번 응용
   ```python
   print("{0:^<+30,}".format(100000000))   # +100,000,000^^^^^^^^^^^^^^^^^^
   
   # <정리해보기>
   # a = '몇번째 글자부터 적용할 것인가? (숫자로만 입력)'
   # b = '빈 공간에는 어떤 문자로 적용할 것인가? (별도의 처리 없이 문자만 입력)'
   # c = '정렬은 어떻게 할 것인가? (>,<,^)(별도의 처리없이 기호만 입력)'
   # d = '양/음수 구분을 할 것인가? (+를 붙일가 말까만 선택하기)'
   # e = '확보하고자 하는 글자의 수'
   # f = '천 단위 숫자 구분기호 표시여부(,를 붙일까 말까만 선택하기)'
   ## " { a : b c d e f } " 
   ```  

4. 소숫점 특정 자리수 까지만 표시 
   ```python
   # 소숫점 세번째 자리에서 반올림하여 표시(둘째짜리까지만 표시하기)
   print("{0:.2f}".format(5/3))
  
   # a = '몇번째 글자부터 적용할 것인가? (숫자로만 입력)'
   # b = '몇번째 자리까지 표시할 것인가(소숫점 한정, n+1번째에서 반올림처리)
   ## " { a : . b f } "
   ```
   

## 파일입출력
1. 파일을 불러오기/생성하여 파일 내 직접적으로 내용을 입력/수정을 할 수 있다.
2. open을 이용하여 파일을 열고/close를 이용해 파일을 닫아준다.
3. '변수명' = open('생성/불러오고자 하는 파일명','불러오고자 하는 형태(r/w/r+/a)','인코딩형태(utf8로 하지 않으면 한글이 오류가 날 수 있음!)')
4. '변수명'.close()하여 파일을 닫는다.

   ```python
   # 쓰기보드
   score_file = open('score.txt', 'w', encoding='utf8')    # 폴더 내 score.txt라는 파일이 없으므로 새로 생성한다. 쓰기모드로 생성되며 인코딩형태는 utf8이다.
   print('수학: 0', file=score_file)                       # score파일 내 '수학: 0'를 입력한다.
   print('영어: 50',file=score_file)                       # score파일 내 '영어: 50'을 입력한다.
   score_file.close()                                      # score파일을 닫는다.
   
   # 추가모드
   score_file = open('score.txt', 'a', encoding='utf8')    # 폴더 내 score.txt라는 파일이 없으므로 새로 생성한다. 추가모드로 생성되며 인코딩형태는 utf8이다.
   score_file.write('과학 : 80')                           # 파일 내 '과학 : 80'이라는 내용을 추가한다.
   score_file.write('\n코딩: 100')                         # 파일 내 '코딩 : 100'이라는 내용을 추가한다. 추가모드에는 별도의 줄바꿈이 존재하지 않으므로 줄바꿈도 수동으로 진행한다.
   score_file.close()                                      # score파일을 닫는다.
   
   # 읽기모드1
   score_file = open('score.txt', 'a', encoding='utf8')    # 폴더 내 score.txt라는 파일을 연다.. 읽기모드로 생성되며 인코딩형태는 utf8이다.
   print(score_file.read())                                # score 파일 내 모든 자료를 읽어온다.
   score_file.close())                                     # score파일을 닫는다.

   # 읽기모드2 (한 줄씩 읽기)   
   score_file = open('score.txt', 'a', encoding='utf8')    # 폴더 내 score.txt라는 파일을 연다.ㄴ 읽기모드로 생성되며 인코딩형태는 utf8이다.
   print(score_file.readline(), end="")                    # 한 줄씩 읽는다. 한 줄 읽고 자동으로 커서는 다음 줄로 이동한다. 만일 출력형태가 줄바꿈이 과도하게 되어 보기 불편하다면 'end = ""'를 통해서 문장의 끝을 줄바꿈으로 처리하지 않도록 바꿈ㄴ다.
   score_file.close())                                     # score파일을 닫는다.

   #읽기모드3 (while문을 이용하여 파일에 존재하는 모든 내용을 읽어들인다)
   score_file = open('score.txt', 'a', encoding='utf8')    # 폴더 내 score.txt라는 파일을 연다.ㄴ 읽기모드로 생성되며 인코딩형태는 utf8이다.
   while True:
       line = score_file.readline()                        # 파일의 내용을 무한대로 한줄씩 읽는다.
       if not line:                                        # 만일 다음 줄이 없다면
           break                                           # 반복문을 빠져나온다
       print(line)                                         # 가정문에 해당하지 않는 한 계속 내용을 한줄씩 출력한다.
   score_file.close()                                      # score파일을 닫는다.
   
   #읽기모드4 (For문을 이용하여 파일에 존재하는 모든 내용을 읽어들인다)
   score_file = open('score.txt', 'a', encoding='utf8')    # 폴더 내 score.txt라는 파일을 연다.ㄴ 읽기모드로 생성되며 인코딩형태는 utf8이다.
   lines = score_file.readliness()                         # 파일 내 모든 내용을 리스트 형태로 저장한다.
   for line in lines:
       print(line, end= "")                                # 리스트 내용만큼 line변수에 대입하여 출력한다.
   
   score_file.close()
   ```
   

## pickle
1. 코드의 자료형태/내용을 별도 파일에 저장하고 그것을 그대로 불러올 수 있는 기능이다.
2. 자료형태가 그대로 남기 때문에 불러오기를 하면 별도의 변환 없이 저장했던 그대로 코드를 사용할 수 있다.
   ```python
   from pickle import *
   profile_file = open('profile.pickle','wb')                              # open을 통하여 파일 생성/열기. open('파일 이름','(불러오는 파일의 타입 지정(wb, rb))')
   profile = {'이름':'박명수','나이':30,'취미':['축구','골프','코딩']}       # profile에 값 저장
   print(profile)
   dump(profile, profile_file)                                             # profile의 값을 profile_file에 저장한다.
   profile_file.close()                                                    # profile_file을 닫는다.
   
   profile_file = open('profile.pickle','rb')                              # open을 통하여 파일 생성/열기. open('파일 이름','(불러오는 파일의 타입 지정(wb, rb))') 
   profile = load(profile_file)                                            # profile에 profile_file에서 로드한 내용을 저장한다.
   print(profile)
   profile_file.close()
   ```
   
## with
1. 자료를 열고 닫을 필요 없이 with를 사용하여 한번에 처리한다.
2. 사용법1(pickle로 사용) : with open('파일명','로드파일형태(rb/wb)') as '파일명에서 불러온 데이터를 저장할 변수명'
3. 사용법2. with open('파일명','로드파일형태(w/r/a/r+),encoding='인코딩형태, 대부분 utf8을 사용') as '파일명에서 불러온 데이터를 저장할 변수명'
   ```python
   from pickle import *
   with open ('profile.pickle','rb') as profile_file:      # profile.pickle이라는 파일을 rb(읽기형태)의 파일로 연다/profile_file이라는 변수에 저장한다.
       print(load(profile_file))                               # profile_file을 불러오면 profile.pickle의 파일을 불러온다.
   
   
   with open('study.txt','w',encoding='utf8') as study_file: # study.txt파일을 '쓰기형태'로 생성하여 study_file변수와 동기화한다.
       study_file.write('파이썬을 열심히 공부하고 있어요')         # study_file변수에 '파이썬을 열심히 공부하고 있어요'라고 쓰면, 동기화한 studu.txt파일에 저장된다
   
   with open('study.txt','w',encoding='utf8') as study_file: # study.txt파일을 '읽기형태'로 불러와하여 study_file변수에 저장한다.
       print(study_file.read())                              # study_file에 저장된 파일을 읽어들인다.
   ```


## 퀴즈7
당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다. 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X주차 주간보고 -

부서 : 

이름 : 

업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오

조건 : 파일명은 '1주차.txt', 2주차.txt',...와 같이 만든다.

<내가 쓴 답>

```python
for i in range(1,51):
   with open(str(i)+'주차.txt','w',encoding='utf8') as t:
      t.write('- {0} 주차 주간보고 -\n'.format(i))
      t.write('부서 : \n')
      t.write('이름 : \n')
      t.write('업무 요약 : ')
```

<정답>
  
```python
for i in range(1, 51):
   with open(str(i) + '주차.txt', 'w', encoding = 'utf8') as report_file:
      report_file.write('- {0} 주차 주간보고 -'.format(i))
      report_file.write('\n부서 : ')
      report_file.write('\n이름 : ')
      report_file.write('\n업무 요약 : ')
```