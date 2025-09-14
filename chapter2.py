# 조건문 (if)
'''
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 찾으세요")
else : 
    print("준비물 필요 없어요")


temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30 :
    print("괜찮은 날씨예요")
elif 0 <= temp < 10 :   # 이렇게도 가능
    print("외투를 챙기세요")
else : 
    print("너무 추워요. 나가지 마세요")
'''

# for문
'''
for waiting_no in range(5): # 0,1,2,3,4
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1,6): # 1,2,3,4,5
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks : 
    print("{0}, 커피가 준비되었습니다." .format(customer))

'''

# while 
'''
customer = "토르"
index = 5
while index >= 1 :
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요." .format(customer, index))
    index -= 1 
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# 무한루프
customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer,index))
    index += 1


customer = "토르"
person = "Unknown"

while person != customer : 
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
'''

# continue & break
'''
absent = [2,5] # 결석
no_book = [7] #책을 안 가져옴
for student in range(1,11) :
    if student in absent:
        continue
    elif student in no_book :
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

'''
# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 -> 101,102,103,104.
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환 
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환 
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

'''
퀴즈) 택시 기사임 
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램
조건 1) 승객별 운행 소요 시간을 5분 ~ 50분 사이의 난수로 정해진다.
조건 2) 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 한다.

'''
from random import *
totalCount = 0
for i in range(51) :
    random = randint(5,51)
    if 5 <= random <= 15 : 
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, random))
        totalCount += 1
    elif 5 > random or random > 15:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,random))
    
    

print("총 탑승 승객 : {0}분".format(totalCount))