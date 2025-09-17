class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# 먼저 전달하는 부모 클래스를 우선으로 한다.
# 여기서 super()는 Unit생성자 
class FlyableUnit(Unit,Flyable):
    def __init__(self):
        # super().__init__() # 이렇게 하면 두 개의 부모 중 먼저 전달한 부모의 생성자만 호출이 됨 
        # 따라서 두 개의 부모 모두 생성자 호출을 하고 싶을 때는 아래처럼 직접 작성해준다.
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()

