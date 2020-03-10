# 객체 출력1 : 피클파일에 저장하기
## pickle (import 선언) : 딕셔너리/리스트와 같은 내용을 파일에 그대로 저장/불러올 수 있다.
## dump() : 객체를 pickle모듈로 압축한다.
import pickle

# 저장하고자 하는 딕셔너리를 입력한다.
gameOption = {'sound' : 8,'videoQuality' : 'high','money' : 1000000, 'weaponlist' : ['gun','missile','knife']}

# 파일을 연다. (해당 예시에서는 이진파일을 호출하였으나, 어느 확장자로 하더라도 피클이 가능하다)
# 피클파일의 모드를 지정할 때에는 반드시 뒤에 'b(바이너리)'를 입력한다(wb, rb ... )
file = open("test1.p",'wb')

#딕셔너리를 피클파일에 저장한다.
pickle.dump(gameOption,file)

#파일을 닫는다.
file.close()
