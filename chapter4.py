# 클래스
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
'''
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(\
        name, location, damage))
    
attack(name, "1시", damage)
attack(tank_name, "2시", tank_damage)
attack(tank2_name, "3시", tank2_damage)


# !!! 위와 같이 계속해서 객체를 만들 수 있지만, 코드의 중복이 일어남 !!! 
# 아래처럼 class로 분리해서 편리하게 객체를 생성할 수 있음
# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name 
        self.hp = hp 
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# __init__ 함수에서 받는 인자만큼 매개변수를 전달해줘야 함

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
# !!! 파이썬에서는 외부에서 객체에 변수를 추가해서 사용할 수 있음 !!!
wraith2.clocking = True 

if wraith2.clocking == True: 
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# wraith2 에는 clocking이라는 필드를 만들었지만, wraith1에는 clocking이라는 필드가 없어서 wraith1.clocking을 하면 오류 남 

# 메소드
# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name    # 여기서 self는 자기자신의 멤버변수를 의미한다.
        self.hp = hp 
        self.damage = damage

    # 메소드
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

    # 메소드
    def damaged(self, damage):
        print("{0} : {1} 데미지를 잃었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 메딕 : 의무병
'''

# 상속
# 부모 클래스
class Unit:
    def __init__(self, name, hp):
        self.name = name 
        self.hp = hp 

# 자식 클래스(자손 클래스)
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    # 메소드
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

    # 메소드
    def damaged(self, damage):
        print("{0} : {1} 데미지를 잃었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 다중 상속 (상속 받은 부모 클래스가 2개 이상)
# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x
# 날 수 있는 기능을 가진 클래스
class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage) # self는 무조건 넣어야 함
        Flyable.__init__(self, flying_speed)


# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# 현재 상속 구조가 
# Unit <- 상속 - AttackUnit 
# AttackUnit <- 상속 - FlyableAttackUnit  - 상속 -> Flyable
# 이런 구조임
