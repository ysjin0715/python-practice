#영한사전 만들기
# english_dict={'one':'하나','two':'둘','three':'셋'}
import sys
english_dict={}
english_dict['one']='하나'
english_dict['two']='둘'
english_dict['three']='셋'

word=input('찾고자 하는 영어단어를 입력하시오(업데이트가 덜되서 원투쓰리밖에 없다구!): ')
print(word, ':', english_dict[word])

k_word=input('찾고자 하는 한글단어를 입력하시오(업데이트가 덜되서 하나둘셋밖에 없다구!): ')
for s in english_dict:
    if k_word==english_dict[s]:
        print(k_word,':',s)
