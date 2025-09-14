# 함수
'''

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance, money): # 입금 함수
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money


balance = 0 #잔액
balance = deposit(balance, 1000)
print(balance)

# 출금 함수
def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else : 
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

balance = 0 #잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance, 1000)
print("수수료 {0}원이며, 잔액은 {1}원입니다." .format(commission, balance))


def profile(name, age, main_lang):
    print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}" .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업 # 함수에 기본값을 적용할 수 있음
def profile(name, age=17, main_lang="파이썬"): 
    print("이름")

def profile(name, age, main_lang):
    print(name, age, main_lang)

# 순서가 뒤바뀌어도 키워드에 해당하는 값을 적어두면 자동으로 해당 키워드의 값으로 전달이 된다.
profile(name="유재석", main_lang="자바", age=20)
'''

# 가변인자
'''
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이 {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)
    
profile("유재석", 20, "Python", "Java","C", "C++", "C#")
profile("김태호", 25, "Java", "", "","","")

# 위처럼 하게 되면 다룰 수 있는 언어가 더 많아지면 함수 자체를 변경해야 하기 때문에 
# 가변 인자를 사용해야 한다.
def profile(name, age, *language):
    print("이름: {0}\t나이 {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java","C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Java")
'''

# 지역변수 & 전역변수
# 가급적 전역변수 사용은 지양
'''
gun = 10
def checkpoint(soldiers): # 경계근무
    # 전역변수
    global gun # 전역 공간에 있는 gun 사용(만약 global을 명시해주지 않으면 오류 남)
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    
print("전체 총: {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soliders):
    gun = gun - soliders
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
checkpoint_ret(gun, 2)
print("남은 총: {0}".format(gun))
'''


'''
Quiz) 표준 체중을 구하는 프로그램을 작성
표준 체중 : 각 개인의 키에 적당한 체중
성별에 따른 공식
남자 : 키(m) * 키(m) * 22 
여자 : 키(m) * 키(m) * 21

조건1) 표준 체중은 별도의 함수 내에서 계산
    * 함수명 : std_weight
    * 전달값 : 키(height), 성별(gender)
조건2) 표준 체중은 소수점 둘째자리까지 표시
키 175cm 남자의 표준 체중은 67.38kg 입니다.


def std_weight(height, gender="여자") :
    # gender : 여자, 남자
    if gender == "여자":
        print(height, gender)
        return height * height * 21
    elif gender == "남자":
        return height * height * 22

height = 1.53
gender = "여자"
result = round(std_weight(height, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, result))
'''

# 표준 입출력
'''
print("Python", "Java", sep=",") # 이렇게 하면 ,로 연결된 값이 공백 없이 값이 연결됨
print("Python", "Java", sep=",", end="? ") # 이렇게 하면 마지막에 
print("무엇이 더 재미있을까요?")

# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).ljust(4), sep=": ")

'''

# zfill(): 인자만큼의 공간을 확보하고 빈값에는 0으로 채워넣는 것 은행 대기순번표
# 001, 002, 003 ... 
'''
for num in range(1,21):
    print("대기번호: " + str(num).zfill(3))
'''
# 사용자 입력을 통해서 가지고 오는 값은 항상 타입이 문자열임
'''
answer = input("아무값이나 입력하세요: ")
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")
'''
# 다양한 출력 포맷
'''
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) # > : 오른쪽 정렬, 10은 10자리를 의미

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움, 양수일 때는 +로, 음수일 때는 -로
print("{0:_<+10}".format(-500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000))
print("{0:,}".format(-100000000))

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기 
# 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기 
print("{0:^<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))
print("{0:2f}".format(5/3))
'''

# 파일 열고 닫기
'''
score_file = open("score.txt", "w", encoding="utf8")
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close() # 파일을 열었으면 닫아줘야 함

score_file = open("score.txt", "a", encoding="utf8") # append 기존 내용에 덧붙인다는 뜻
score_file.write("과학: 80")
score_file.write("\n코딩: 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r : 읽어온다는 의미
# print(score_file.readline())  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())


# 파일이 몇 줄인지 모를 경우
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="") # 줄바꿈을 하기 싫다면 end="" 해주기 !!

score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list형태로 저장
for line in lines:
    print(line, end="")

score_file.close()

# pickle (프로그램에서 사용하는 데이터를 파일 형태로 저장해주는 것)
import pickle
profile_file = open("profile.pickle", "wb") # pickle을 사용하기 위해서는 무조건 b(바이너리) 형식으로 열어줘야 한다. 그래서 wb 임
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"] }
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)

profile_file.close()



# with (파일을 열기 -> 처리 -> 파일 닫기) --> with문을 사용하면 열었던 파일을 닫아줄 필요가 없음
import pickle
with open("profile.pickle", "rb") as profile_file: # profile.pickle을 읽어서 profile_file 변수에 저장을 해준 뒤,
    print(pickle.load(profile_file))    # profile_file에 있는 정보를 불러옴


with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

'''

'''
Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- x 주차 주간보고 - 
부서 :
이름 : 
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오. 
조건: 파일명은 '1주차.txt', '2주차.txt' , .... 와 같이 만듭니다.
'''

# 내가 푼 방법
'''
week = 1
while True: 
    if week > 50:
        break
    file_name = str(week) + "주차.txt"
    with open(file_name, "w", encoding="utf=8" .format(week)) as report_file:
        report_file.write("- {0} 주차 주간보고 - ".format(week))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")
    
    week += 1


# 풀이
for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 - ".format(week))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")
'''