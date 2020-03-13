# 객체 생성하기
# 객체 = 변수 + 메소드
# 객체의 속성은 객체 안의 변수로 저장되며, 객체의 이름 + '.' 이후 변수의 이름을 적는다. (예 : object.speed)
# 객체의 속성은 내부의 멤버변수 + 메소드로 구성된다. (class 내 모든 변수 및 함수를 속성이라고 일컫는다)

# 객체의 동작을 메소드라고 한다. 메소드는 객체 안에 정의된 함수로 객체 + '.' 이후 함수명으로 호출한다. (예 : object.drive())
# 메소드는 class 내부 함수를 말한다.

# 멤버변수는 해당 class의 값을 지정해주는 모든 변수를 말한다.

# class Car:
#    def drive(self):           # 객체의 '속성'
#       self.speed = 10         # 객체의 '메소드'

# 객체의 생성
# myCar = Car()

# myCar의 속성 추가(멤버변수의 추가)
# myCar.color = 'blue'
# myCar.model = 'E-Class'

# 자동차 객체의 속성/메소드 사용
# myCar.drive()                 # Car의 인스턴스인 myCar 내에 저장되어있는 drive 속성 호출
# print(myCar.speed)            # 호출된 drive 속성에서 speed값 출력


class Car:                       # 클래스 정의
   def drive(self):              # 메소드 생성
      self.speed = 60

myCar = Car()                    # Car 인스턴스/객체 생성

myCar.speed = 0                  # myCar만의 속성(멤버변수) 설정
myCar.model = 'E-Class'          # myCar 멤버변수 설정2

myCar.color = 'blue'             # myCar 멤버변수 설정3
myCar.year = '2017'              # myCar 멤버변수 설정4

print('자동차 객체를 생성하였습니다.')
print('자동차의 속도는',myCar.speed)      # myCar 속성 출력
print('자동차의 색상은',myCar.color)

print('자동차의 모델은',myCar.model)
print('자동차를 주행합니다.')
myCar.drive()                            # Car class의 drive 속성 호출
print('자동차의 속도는',myCar.speed)      # drive속성의 메소드 호출
