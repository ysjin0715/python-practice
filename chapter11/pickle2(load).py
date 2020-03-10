# pickle : 피클파일 출력하ㅣㄱ
import pickle

# 파일을 읽개 형태로 열어 file변수에 저장한다.
file = open('test1.p','rb')

# file을 피클함수를 통해 로드하여 obj에 저장한다.
obj = pickle.load (file)

# obj를 출력한다.
# 피클에 저장했던 내용 그대로 출력되는 것을 알 수 있다.
print(obj)