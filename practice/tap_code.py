# 이중리스트
tap_code = [['a','b','c','d','e'],
            ['f','g','h','i','j'],
            ['l','m','n','o','p'],
            ['q','r','s','t','u'],
            ['v','w','x','y','z']]

result = []

# 문자열 리스트화/공백제거
text = input('변환하려는 영어를 입력하시오: ')
text = text.replace(" ","").lower()
text_list = list(text)

# 인코딩
def find_index(c):
   for i in range(len(tap_code)):
      for j in range(len(tap_code[i])):
         if c == tap_code[i][j]:
            result.append(i+1)
            result.append(j+1)
            return result

for t in text_list:
   print(t)
   find_index(t)

print(result)


# 디코딩
number = input('변환하려는 탭 코드의 번호를 입력해주세요: ')
number = number.replace(' ','')
number_list = list(number)