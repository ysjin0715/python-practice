# 1. 파일에 데이터 쓰기/생성하기
## 1. 쓰기모드 : w  * 생성하고자 하는 파일과 같은 이름의 파일이 폴더 내 있을 경우, 기존의 데이터가 사라질 수 있음!

outfile = open('phones2.txt','w',encoding = 'utf8')

outfile.write('홍길동 010-1234-5678\n')               # 쓰고자 하는 문장 뒤에 \n을 넣어 줄바꿈을 시켜줄 수 있다.
outfile.write('김철수 010-1234-5679\n')
outfile.write('김영희 010-1234-5680\n')

outfile.close()