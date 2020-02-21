import random
quote=[]
quote.append('가는 날이 장날이다')
quote.append('강물도 쓰면 준다')
quote.append('거미도 줄을 쳐야 벌레를 잡는다')
quote.append('다 된 밥에 재뿌리기')
quote.append('닭에게는 보석이 보리알만 못하다')
quote.append('말 안하면 귀신도 모른다')

a=int(len(quote))
b=random.randrange(a)


#출력하기
print('#'*14)
print('#','오늘의 속담','#')
print('#'*14)
print("")
print(quote[b])

#답지
# daily=random.choice(quote)
# print(daily)