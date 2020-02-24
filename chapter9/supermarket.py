#편의점 재고 관리
import sys

item={'종이컵':2,'우유':1}
item['커피음료']=7
item['펜']=3
item['책']=5
item['콜라']=4

print('재고관리시스템을 실행합니다')
key=input('물건의 이름을 입력하시오: ')
print(item[key])

s= input('변경하고자 하는 재고를 입력하시오: ')
print('선택된 물품:',s)
v= int(input('재고의 증가/감소량을 적어주세요: '))
if item[s]+v<0:
    print('재고의 양은 0미만으로 설정될 수 없습니다.')
    print('재고관리시스템을 강제종료합니다.')
    sys.exit()
else:
    item[s]=item[s]+v
    print('재고의 값이',item[s],'로 변경되었습니다.')
