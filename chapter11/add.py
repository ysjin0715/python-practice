# 파일에 데이터 추가하기
## 1. 쓰기모드 : a

outfile = open('phones.txt','a',encoding = 'utf8')

outfile.write('강감찬 010-1234-5681\n')
outfile.write('김유신 010-1234-5682\n')
outfile.write('정약용 010-1234-5683\n')

outfile.close()