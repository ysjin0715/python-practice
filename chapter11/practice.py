# 1. 사용자가 입력한 텍스트 파일을 열어서 파일 안에 글자가 몇 개나 있는지 계산하는 프로그램 만들기
from pickle import *


def practice1():
   filename = input('파일 이름을 입력하세요 : ')
   infile = open(filename, 'r')
   show = 0
   for line in infile:
      show = len(line)

   print('파일 안에는 총',show,'개의 글자가 있습니다')
   infile.close()

def practice2():
   filename = input('파일 이름을 입력하시오: ')
   re = input('변경할 내용을 입력하세요: ')
   infile = open(filename,'r+',encoding='utf8')
   a = infile.read().rstrip()

   if a.find(re) == -1:
      print('변경할 내역이 없습니다')

   else:
      infile.seek(0)           # 파일 작업지점 변경
      a = a.replace(re,'')
      infile.write(a)
      print(a)
      print('변경된 파일이 저장되었습니다.')

   infile.close()

def practice3():
   filename = input('파일 이름을 입력하시오: ')
   infile = open(filename, 'r', encoding = 'utf8')
   dict = {}

   for line in infile:
      for ch in line:
         if ch in dict:
            dict[ch] += 1

         else:
            dict[ch] = 1

   print(dict)
   infile.close()

def practice4():
   num0 = 12
   num1 = 3.14
   num2 = [1, 2, 3, 4, 5]
   with open('test.bat','wb') as infile:
      dump(i, infile)
      dump(num1, infile)
      dump(num2, infile)

   with open('test.bat','rb') as infile1:
      a = load(infile1)
      b = load(infile1)
      c = load(infile1)
      print(a)
      print(b)
      print(c)

