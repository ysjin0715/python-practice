# 파일 복사하기
from sys import *
from os import *
from io import *

def search_items(dirname):             # 해당 경로 내 있는 파일을 리스트형태로 보여준다.
   global file_list                    # 전역변수 file_list를 가져온다
   file_list = listdir(dirname)        # file_list에 listdir을 이용하여 파일이름을 리스트형태로 변환한다.
   return file_list                    # 최종결과물을 반환한다.

file_list = []
file_name1 = input('복사할 파일명: ')
file_name2 = input('복사당할 파일명(없으면 새로 생성) : ')

search_items('C:\\python\\python-practice\\chapter11')

if file_name1 not in file_list:
   print('복사할 파일이 존재하지 않습니다.')
   exit()

else:
   infile1 = open(file_name1,'r',encoding = "utf8")
   infile2 = open(file_name2,'w',encoding = "utf8")

   a = infile1.read()
   infile2.write(a)

   infile1.close()
   infile2.close()

infile2 = open(file_name2, 'r', encoding='utf8')

b = infile2.read()

print(b)