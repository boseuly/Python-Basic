# 예외처리
'''
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))

    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러 발생, 잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)
'''

# 한 자리 숫자에 대해서만 나누기해주는 계산기
# 필요한 경우 에러를 발생시키기 
'''
try:
    print("한자리 숫자 전용 나누기 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError # 고의로 에러를 발생시킴
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
'''

# 에러 정의하기
'''
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg


try:
    print("한자리 숫자 전용 나누기 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 고의로 에러를 발생시킴
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:   # err = 위에서 BigNumberError에 저장한 msg
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally: # 무조건 마지막에 실행되는 구문(에러가 발생해도 실행됨)
    print("계산기를 이용해 주셔서 감사합니다.")
'''
