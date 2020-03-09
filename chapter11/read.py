# 1. 파일에서 데이터 읽기
## 1. open('파일명/파일 경로','모드 선택(r/w/a/r+)
## r : 파일의 읽기모드
## w : 파일의 쓰기모드. 파일의 처음부터 쓰기 시작한다.
## a : 파일의 추가모드, 파일의 끝부분부터 쓰기 시작한다.
## r+ : 파일의 일기/쓰기모드. 모드를 변경하기 위해서는 seek()함수가 호출되어야 한다.

infile = open('phones.txt','r',encoding='utf8')                                                    # 디렉토리 내 파일이 존재할 경우
infile2 = open('C:\\python\\python-practice\\chapter11\\phones.txt','r',encoding='utf8')           # 디렉토리 내 파일이 존재하지 않을 경우


# 2. 파일에서 전체 데이터 읽기
## .read('읽고 싶은 문자의 개수(생략가능)')
a = infile.read()
b = infile2.read(10)
print(a)
print(b)

##.readline() : 한 줄씩 읽기
## rstrip() : 줄바꿈 포함 오른쪽 공백 지우기
c = infile.readline()
while c != "":
   print(c)
   c = infile.readline()               # 엔터가 포함된 채로 출력된다.

d = infile.readline().rstrip()
while d != "":
   print(d)
   d = infile.readline().rstrip()      # 엔터가 포함되지 않은 채로 깔끔하게 출력된다.


# 3. 파일에서 데이터 닫기
## .close() * 파일을 닫지 않을 시 추후 파일접근이 어려울 수 있음!
infile.close()
infile2.close()