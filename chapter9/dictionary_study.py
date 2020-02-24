#1. 딕셔너리란?
#거대한 딕셔너리 내부 키-값이 연결된다. (키 값 쌍)
#공백 리스트는 []로 생성하나 딕셔너리는 {}로 생성한다.
phone_book={}
phone_book['홍길동']="010-1234-5678"
print(phone_book)

#처음 딕셔너리를 생성할 때 키와 값을 모두 넣는 것도 가능한다.
#dd={'홍길동':'010-1234-5678'}
phone_book['강감찬']='010-1234-5679'
phone_book['이순신']='010-1234-5680'

print(phone_book)


#2.딕셔너리 연산
#키를 이용하여 그와 연관된 값을 찾을 수 있다.
print(phone_book['강감찬'])

#딕셔너리에서 사용되는 모든 키를 출력하려면 keys()를 사용한다.
print(phone_book.keys())

#딕셔너리에서 사용되는 모든 값을 출력하려면 values()를 사용한다.
print(phone_book.values())

#리스트와 마찬가지로 딕셔너리도 어떤 유형의 값도 저장할 수 있다.
#정수, 문자열, 다른 리스트, 다른 딕셔너리도 저장할 수 있다.

#딕셔너리의 모든 항목을 방문하면서 출력하기(for문 이용)
for key in sorted(phone_book.keys()):
    print(key,phone_book[key])
    
#딕셔너리 내 항목 삭제하기(del이용)
del phone_book['홍길동']
print(phone_book)

#딕셔너리 내 모든 항목 삭제하기(clear이용)
phone_book.clear()
print(phone_book)