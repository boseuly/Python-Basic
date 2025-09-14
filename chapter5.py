# 연산자 오버로딩
# 부모클래스에서 정의된 메소드가 아닌 자식 클래스에서 정의된 메소드를 사용하고 싶을 때
# 메소드를 새롭게 정의하는 것을 오버로딩이라고 함

# 상속
# 부모 클래스
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name 
        self.hp = hp 
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 자식 클래스(자손 클래스)
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
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


# 날 수 있는 기능을 가진 클래스
class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        Flyable.__init__(self, flying_speed)

# 벌처 : 지상 유닛, 기동서이 좋음
vulture = AttackUnit("벌처", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("3시")
battlecruiser.fly(battlecruiser.name, "9시")
# 각각 유닛이 공중 유닛인지, 지상 유닛인지 구분을 한 다음에 알맞은 함수를 사용해줘야 함
# 귀찮으니 이걸 연산자 오버라이딩 해준다.



