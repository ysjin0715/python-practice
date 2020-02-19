#암호화와 복호화
#암호화
plain_text=input('암호화할 문장을 입력하시오(영어): ')
q=input('암호화를 진행합니까?(예/아니오): ')
encryted_text=""
if q=="예":
    for a in plain_text:
        x=ord(a)
        x+=1
        y=chr(x)
        encryted_text+=y

else:
    print('암호화/복호화 프로그램을 종료합니다')

#암호문 완성
print(encryted_text)
answer_text=""
q2=input('이어서 복호화를 진행하시겠습니까?(예/아니오): ')


#복호화
if q2=="예":
    for b in encryted_text:
        x1=ord(b)
        x1-=1
        y1=chr(x1)
        answer_text+=y1
    print(answer_text)
    print('암호화/복호화가 완료되었습니다.')

else:
    print('암호화가 완료되었습니다.')