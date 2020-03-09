# 파일에서 단어 읽기
## .split() : 띄어쓰기를 기준으로 문장에서 단어를 추출한다.
f = open('phones3.txt','w',encoding='utf8')
f.write('show me the money')
f.close()

f1 = open('phones3.txt','r',encoding='utf8')
for line in f1:                  # line변수에 f1파일을 대입한다.
   line = line.rstrip()          # line변수 = f1파일에서 대입된 line에서 오른쪽 공백을 없앤 것이다. (문장에서 오른쪽 공백을 없앰)
   print(line)
   word_list = line.split()      # word_list는 line변수에 저장된 f1의 파일내용을 '공백 기준으로 분리'하여 저장한 것이다. (리스트 형태로 저장됨)
   print(word_list)
   for word in word_list:        # word 변수에 word_list 내용을 저장한다.
      print(word)                # word 변수를 출력한다. (=word_list의 내용을 하나씩 출력)
f.close()
