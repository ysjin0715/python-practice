# 클래스
## 객체를 생성하기 위해 변수와 메소드를 정의하는 일종의 틀
```python
class unit:
   def __init__(self, name, hp, damage):
      self.name = name
      self.hp = hp
      self.damage = damage
      print('{0} 유닛이 생성되었습니다.'.format(name))
      print('체력 {0}, 공력격 {1}'.format(self.hp, self.damage))

marine1 = unit('마린',40 ,5)
marine2 = unit('마린',40 ,5)
tank = unit('탱크',150,35)
```

## 객체/인스턴스
1. 객체 : class로 생성된 모든 정보 (위 예시 코딩에서 marine, tank 등)
2. 인스턴스 : class로부터 만들어진 모든 객체를 'class의 인스턴스'라고 말함.
3. 인스턴스를 생성하기 위해서는 class 내 지정된 __init__다음의 조건을 모두 만족해야 함. (self를 제외한 다음의 조건)
4. 다음 조건을 만족하지 못할 경우 오류값을 반환한다.
```python
class unit:
   def __init__(self, name, hp, damage):
      self.name = name
      self.hp = hp
      self.damage = damage
      print('{0} 유닛이 생성되었습니다.'.format(name))
      print('체력 {0}, 공력격 {1}'.format(self.hp, self.damage))

marine1 = unit('마린',40 ,5)          # 객체/ unit 클래스의 인스턴스
marine2 = unit('마린',40 ,5)          # 객체/ unit 클래스의 인스턴스
tank = unit('탱크',150,35)            # 객체/ unit 클래스의 인스턴스
```

## 멤버변수
1. 객체/해당 클래스의 인스턴스 내 저장된 변수
2. self를 제외한 \_\_init\_\_ 다음에 적힌 조건에 대입된 변수를 말한다.
3. 객체/해당 클래스의 인스턴스가 생성되면 클래스 바깥에서도 객체 내 저장된 변수를 꺼내서 쓸 수 있다.
4. 클래스 바깥에서도 객체에 새로운 함수를 class 외부에서 추가로 할당하여 사용할 수 있다.

```python
class unit:
   def __init__(self, name, hp, damage):
      self.name = name
      self.hp = hp
      self.damage = damage
      print('{0} 유닛이 생성되었습니다.'.format(name))
      print('체력 {0}, 공력격 {1}'.format(self.hp, self.damage))

wraith1 = unit('레이스', 80, 5)
# class 바깥에서도 객체 내 저장된 변수를 쉽게 꺼내서 사용할 수 있다!
print('유닛 이름: {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage))

# class 바깥에서도 해당 변수에 저장된 내용 외 새로운 함수를 class 외부에서 추가로 할당할 수 있다.
wraith2 = unit('빼앗은레이스', 80, 5)
wraith2.clocking = True                      # wraith2에 clocking=True라는 새로운 변수를 class 외부에서 추가로 할당하였다!

if wraith1.clocking == True:                 # wraith1에는 clocking이라는 항목이 존재하지 않으므로 오류를 출력한다.
    print('{0}는 현재 클로킹 상태입니다.'.format(wraith1.name))

if wraith2.clocking == True:                 # wraith2에는 clocking이라는 항목이 추가로 할당되었기 때문에 if문이 작동한다.
    print('{0}는 현재 클로킹 상태입니다.'.format(wraith2.name))
```

## 메소드
1. 메소드는 class를 구성하는 함수이다.
2. 메소드 앞에는 기본적으로 self라는 변수를 먼저 넣는다.
```python
# self.이라고 적힌 변수는 __init__의 변수를 가져다 쓴다는 것을 의미한다.
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

# attack 메소드 생성
    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]'.format(self.name, location, self.damage))

# damaged 메소드 생성
    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))

firebat1 = AttackUnit('파이어벳', 50, 16)              # 유닛을 생성한다.
firebat1.attack('5시')                                 # class 내 attack메소드를 활용한다.


firebat1.damaged(25)                                   # class 내 damaged메소드를 활용한다.
firebat1.damaged(25)                                   # 이미 damaged로 변한 hp의 값을 저장하여 그대로 활용하는 것을 알 수 있다.
```

## 상속
1. 위의 class와 아래의 class 안에 포함된 변수가 일부 겹칠 경우, 타 class로부터 변수를 받아 사용할 수 있다.
2. 타 class에 선언된 변수를 사용할 경우에는 먼저 생성된 클래스 내 사용할 클래스의 이름을 넣어주고
3. 변수를 받아서 사용할 메소드 내에 별도로 init을 선언한다.
4. 상속을 해주는 클래스를 '부모클래스'라고 한다.
5. 상속을 받는 클래스를 '자식클래스'라고 한다.
6. (1) class '클래스 이름'(부모클래스 이름)
7. (2) def \_\_init\_\_(self, 변수1, 변수2, 변수3)
8. (3) 자식 클래스명.\_\_init\_\_(self, 받아서 사용할 변수1, 받아서 사용할 변수2)


```python
# (1) class '클래스 이름'(변수를 받아서 이용할 클래스명)
# (2) def __init__(self, 변수1, 변수2, 변수3)
# (3) 변수를 받아서 이용할 클래스명.__init__(self, 받아서 사용할 변수1, 받아서 사용할 변수2)

class unit:                                                 # 사용될 객체를 생성한다.
   def __init__(self, name, hp):                            # 해당 객체와 다음 객체에서는 name과 hp 변수가 겹친다.
      self.name = name
      self.hp = hp


class AttackUnit(unit):                                     # AttackUnit 클래스는 unit클래스의 변수를 받아서 사용한다.
    def __init__(self, name, hp, damage):                   # class의 __init__ 내부에는 self.name과 같은 변수가 없음에도 정상작동한다.
        unit.__init__(self, name, hp)                       # unit의 name값과 hp값을 받아 사용한다.
        self.damage = damage

    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]'.format(self.name, location, self.damage))

    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))

firebat1 = AttackUnit('파이어벳', 50, 16)                    # 변수는 정상작동하는 걸 확인할 수 있다.
firebat1.attack('5시')
```

## 다중상속
1. 부모클래스는 다수가 될 수도 있다.

```python
class unit:
   def __init__(self, name, hp):
      self.name = name
      self.hp = hp


class AttackUnit(unit):
    def __init__(self, name, hp, damage):                   # class의 __init__ 내부에는 self.name과 같은 변수가 없음에도 정상작동한다.
        unit.__init__(self, name, hp)                       # unit의 name값과 hp값을 받아 사용한다.
        self.damage = damage

    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]'.format(self.name, location, self.damage))

    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))


class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed


    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))


class flyable_attack_unit(AttackUnit,flyable):           # AttackUnit, flyable 클래스에서 내용을 상속받는다.
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        flyable.__init__(self, flying_speed)


valkyrie = flyable_attack_unit('발키리', 200, 6, 5)      # flyable_attack_unit 클래스가 무사히 작동된다.
valkyrie.fly(valkyrie.name, '3시')                       # 
```


## 연산자 오버로딩
1. 오버로딩 : 자식클래스에서 정의된 메소드를 사용할 때 메소드를 새롭게 정의하여 사용이 가능하다.
2. 오버로딩을 통하여 메소드를 재정의 시 부모클래스에서 정의된 메소드가 아닌 자식클래스에서 정의된 메소드가 출력된다.


```python
class unit:
   def __init__(self, name, hp, speed):
      self.name = name
      self.hp = hp
      self.speed = speed

   def move(self, location):
       print('[지상 유닛 이동]')
       print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'. format(self.name, location, self.speed))


class AttackUnit(unit):
    def __init__(self, name, hp, speed, damage):                   # class의 __init__ 내부에는 self.name과 같은 변수가 없음에도 정상작동한다.
        unit.__init__(self, name, speed, hp)                       # unit의 name값과 hp값을 받아 사용한다.
        self.damage = damage

    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]'.format(self.name, location, self.damage))

    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))


class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed


    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))


class flyable_attack_unit(AttackUnit,flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        flyable.__init__(self, flying_speed)

    def move(self, location):                      # 오버로딩
        print('[공중 유닛 이동]')
        self.fly(self.name, location)

vulture = AttackUnit('벌쳐',80, 10, 20)

battlecruiser = flyable_attack_unit('배틀크루저', 500, 25, 3)

vulture.move('11시')
battlecruiser.move('9시')                        # Unit의 메소드가 출력되는게 아닌 flyable_attack_unit에서 오버로딩하여 재정의된 메소드가 출력된다.
```


## pass
1. 클래스 내 메소드에 별도의 지정을 하지 않아도 일단 넘어가도록 지정해줄 수 있다.
2. 클래스 뿐만 아니라 함수 내에서도 사용가능하다.

```python
class unit:
   def __init__(self, name, hp, speed):
      self.name = name
      self.hp = hp
      self.speed = speed

   def move(self, location):
       print('[지상 유닛 이동]')
       print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'. format(self.name, location, self.speed))


class Buildingunit(unit):  `                        # Buildingunit은 unit의 자식 클래스이다.
    def __init__(self, name, hp, location):         # unit으로부터 name, hp, location값을 받아온다.
        pass                                        # 나머지는 그냥 넘어간다.


supply_depot =  Buildingunit('서플라이 디폿', 500, '7시')       # 값만 받고 나머지는 그냥 넘어갔음에도 정상적으로 함수가 작동되는 걸 볼 수 있다.

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')


def game_over():
    pass

game_start()
game_over()                                          # 함수 내 별도로 지정된 값이 없음에도 정상적으로 함수가 작동한다!
``` 


## super
1. 부모클래스로부터 상속을 받을 때, 자식클래스에서는 상속받는 부모클래스의 이름이 아닌, super()로 간단하게 선언할 수 있다.
2. super().__init__(상속받을 변수1, 상속받을 변수2...)로 표현하며, super로 값을 받을 시 self는 적지 않는다.
    ```python
    class Buildingunit(unit):
        def __init__(self, name, hp, location):
           # Unit.__init__(self, name, hp, 0)
           super().__init__(name, hp, 0)            # super().으로 대신 상속을 받아왔음에도 정상적으로 값을 받아올 수 있다.
           self.location = location
    ```
   
* 그러나 다중상속을 받는 클래스의 경우, super를 사용하면 두 값을 모두 받지 못하고 첫번재로 적힌 부모클래스의 값만 받아오는 오류가 생긴다.
* 그러므로 다중상속을 할 경우 super가 아닌 일반적인 방법으로 상속을 받아야 한다.
```python
class unit1:
    def __init__(self):
        print('unit 생성자')           # unit1의 상속을 받았는지 확인하는 출력문

class flyable1:
    def __init__(self):
        print('flyable 생성자')        # flyable1의 상속을 받았는지 확인하는 출력문

class flyableunit1(flyable1, unit1):
    def __init__(self):                # 두 클래스의 상속을 받되
        super().__init__()             # super() 하나로만 받는 클래스

class flyableunit2(flyable1, unit1):
    def __init__(self):                # 두 클래스의 상속을 받되
        flyable1.__init__(self)        # 일반적인 방법으로 두 클래스를 모두 받는다.
        unit1.__init__(self)


dropship = flyableunit1()              # 'flyable 생성자'라고만 뜨며 두 값을 모두 받지 못한다.
dropship2 = flyableunit2()             # 두 개의 클래스 내용이 모두 출력되며 두 값을 모두 받을 수 있음을 알려준다.
```

## 클래스의 활용
* isinstance('변수명', '클래스명') : 해당 변수가 해당 클래스로 쓰였는가를 검사하는 변수
```python
from random import *

class unit:                                                        # class AttackUnit의 부모클래스
   def __init__(self, name, hp, speed):
      self.name = name
      self.hp = hp
      self.speed = speed
      print('{0} 유닛이 생성되었습니다.'.format(name))

   def move(self, location):
       print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'. format(self.name, location, self.speed))

   def damaged(self, damage):
       print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
       self.hp -= damage
       print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
       if self.hp <= 0:
           print('{0} : 파괴되었습니다.'.format(self.name))


class AttackUnit(unit):                                            # class unit의 자식클래스/flyable_attack_unit의 부모클래스
    def __init__(self, name, hp, speed, damage):                   # class의 __init__ 내부에는 self.name과 같은 변수가 없음에도 정상작동한다.
        unit.__init__(self, name, speed, hp)                       # unit의 name값과 hp값을 받아 사용한다.
        self.damage = damage

    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]'.format(self.name, location, self.damage))


class flyable:                                                     # flyable_attack_unit의 부모클래스2 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed


    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))


class flyable_attack_unit(AttackUnit,flyable):                     # AttackUnit, flyable의 자식클래스
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


# 마린 설계도
class marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, '마린', 40, 1, 5)

    def stimpack(self):                                            # 스팀팩 기능 구현
        if self.hp >10:
            self.hp -= 10
            print('{0}: 스팀팩을 사용합니다. (hp 10 감소)'.format(self.name))

        else:
            print('{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.'.format(self.name))


# 탱크 설계도
class Tank(AttackUnit):                                            
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, '탱크', 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print('{0} : 시즈모드로 전환합니다.'.format(self.name))
            self.damage *= 2
            self.seize_mode = True

        else:
            print('{0} : 시즈모드를 해제합니다..'.format(self.name))
            self.damage /= 2
            self.seize_mode = False

# 레이스 유닛 설계도
class Wratih(flyable_attack_unit):
    def __init__(self):
        flyable_attack_unit.__init__(self, '레이스', 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print('{0} : 클로킹 모드를 해제합니다.'.format(self.name))
            self.clocked = False

        else:
            print('{0} : 클로킹 모드를 설정합니다.'.format(self.name))
            self.clocked = True

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')


def game_over():
    print('player : gg')
    print('[player] 님이 게임에서 퇴장하셨습니다.')

# 게임 실행
game_start()

# 마린 3기 생성
m1 = marine()
m2 = marine()
m3 = marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wratih()

# 일괄 통솔지정  / 생성된 모든 객체를 attack_unit이라는 리스트로 묶는다.
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 유닛 이동  / for문을 이용하여 유닛 하나하나에 1시로 유닛을 이동시킨다.
for unit in attack_units:
    unit.move('1시')

# 특수능력 개발   /  Tank class에 있던 Tank.seize_developped를 True로 만들어 모든 탱크 개체의 시즈모드를 활성화시킨다.
Tank.seize_developed = True               # t1.seize_developed = True 식으로 t1의 값만 바꿀 수는 없다.
print('[알림] 탱크 시즈모드 개발이 완료되었습니다.')

# 특수능력 사용
for unit in attack_units:                 # 일괄 통솔된 유닛 내 유닛들 기준으로
    if isinstance(unit, marine):          # marine이라는 클래스를 사용하는 유닛이 있다면
        unit.stimpack()                   # stimpack이라는 클래스 내 메소드를 활성화한다.

    elif isinstance(unit, Tank):          # Tank라는 클래스를 사용하는 유닛은
        unit.set_seize_mode()             # set_seize_mode를 활성화한다.

    elif isinstance(unit, Wratih):        # Wraith라는 클래스를 사용하는 유닛은
        unit.clocking()                   # clocking이라는 메소드를 활성화한다.


# 공격 개시
for unit in attack_units:                 # 일괄 통솔된 유닛 내 유닛을 기준으로
    unit.attack('1시')                     # unit 클래스 내 attack이라는 메소드를 활성화한다.

# 피해상황
for unit in attack_units:                 # 일괄 통솔된 유닛 내 유닛들을 기준으로
    unit.damaged(randint(5, 21))          # unit 클래스 내 damaged 메소드를 5~20의 숫자 중 랜덤값을 넣어 활성화한다.

# 게임 종료
game_over()
```


## 퀴즈8
* 주어진 코드를 활용하여 부동산 프로그램을 작성하라
* 출력예제
1. 총 3대 매물이 있습니다.
2. 강남 아파트 매매 10억 2010년
3. 마포 오피스텔 전세 5억 2007년
4. 송파 빌라 월세 500/50 2000년
---
* 내가 쓴 답
```python
class House:
    # 매물의 정보 생성
    def __init__(self, location, house_type, deal_type, price1, price2, completion_year):
       self.location = location
       self.house_type = house_type
       self.deal_type = deal_type
       self.price1 = price1
       self.price2 = price2
       self.completion_year = completion_year

    # 매물의 정보 표시
    def show_detail(self):
        if self.deal_type == '월세':
            print(self.location, self.house_type, self.deal_type, self.price1,'/',self.price2, self.completion_year)

        else:
            print(self.location, self.house_type, self.deal_type, self.price1, self.completion_year)


h = []
gangnam = House('강남','아파트','매매','10억',0,'2010년')
mapo = House('마포','오피스텔','전세','5억',0,'2007년')
songpa = House('송파','빌라','월세',500,50,'2000년')

h.append(gangnam)
h.append(mapo)
h.append(songpa)

s = len(h)

print('총 {}대의 매물이 있습니다.'.format(s))
gangnam.show_detail()
mapo.show_detail()
songpa.show_detail()
```
---
* 정답
```python
class House:
   def __init__(self, location, house_type, deal_type, price, completion_year):
      self.location = location
      self.house_type = house_type
      self.deal_type = deal_type
      self.price = price
      self.completion_year = completion_year


   def show_detail(self):
      print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House('강남','아파트','매매','10억','2010년')
house2 = House('마포','오피스텔','전세','5억','2007년')
house3 = House('송파','빌라','월세','500/50','2000년')


houses.append(house1)
houses.append(house2)
houses.append(house3)


print('총 {}대의 매물이 있습니다.'.format(len(houses)))
for house in houses:
   house.show_detail()
```