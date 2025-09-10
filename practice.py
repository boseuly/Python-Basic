# 숫자형
'''print(5)
print(-10)
print(3.14)
print(2*8)
print(3*(3+1))'''

# 문자열
'''print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)'''

# boolean
'''print(5 > 10) # False
print(5 < 10) # True
print(True)
print(False)
print(not True) # False'''

# 변수
'''animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3
print("우리집" + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 좋아해요") # str() : 숫자를 문자열로 변환 -> 안 그럼 오류 발생
print(name + "는 어른일까요? " + str(is_adult)) 

print(name, "는 ", age, "살이며", hobby, "을 좋아해요")'''
# , : 자동 띄어쓰기 + 자동 자료형 반환(str() 필요 없음)

''' 이렇게 하면 여러 문장 주석 처리 가능 '''

'''station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")'''

# 연산자
'''print(1 + 1)
print(3-2)
print(5%3)
print(10%3)
print(5//2) # 몫: 2
print(10//3) # 몫: 3
print(10 > 3)
print(4 >= 7) 
print(4+3 >= 10) # False
print(1 != 3) # True
print(not(1 != 3)) # False
print((3 > 0) and (3 < 5)) # True
print((3 > 0) or (3 > 5)) # True
print(5 > 4 > 7) # False

number = 2 + 3 * 4
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)
number %= 5 # 1
print(number)
'''
'''
print(abs(-5))  # 5 절대값
print(pow(4,2)) # 4^2 = 4*4 = 14 
print(max(5,12)) # 12 
print(min(5,12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 4 내림
print(ceil(3.14)) # 4 올림
print(sqrt(16)) # 4 제곱근
'''

# 랜덤
'''
from random import * 
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성 
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))   # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 45) + 1)

print(randrange(1,46)) # 1~45 마지막 인자 미포함
print(randint(1,45)) # 1~45 마지막 인자 포함
'''

'''
조건1: 랜덤으로 날짜를 뽑아야 한다. 
조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28일이내로 정함
조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외 
(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

result = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월", result, "일로 선정되었습니다.")
'''

# 문자열
'''
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3) # 줄바꿈 적용 가능
'''

# 슬라이싱
'''jumin = "990515-1234567"
print("성별: " + jumin[7])
print("연: " + jumin[0:2]) # 0~1까지 
print("월: " + jumin[2:4]) # 2~3까지 
print("일: " + jumin[4:6]) # 4~5까지
print("생년월일: " + jumin[:6]) # 처음부터 6 직전까지 
print("뒤 7자리: " + jumin[7:14]) # 7부터 13까지
print("뒤 7자리: " + jumin[7:]) # 7부터 끝까지'''

# 문자열 처리함수
'''python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("Java")) # 내가 원하는 문자가 없을 경우 -1을 반환 
print(python.index("Java")) # 내가 찾는 문자가 없을 경우 에러를 뱉음
'''

# 문자열 포맷
'''
print("a" + "b")
print("a", "b")
'''

'''
# 방법 1

print("나는 %d살입니다." % 20) # 정수
print("나는 %s을 좋아해요" % "파이썬") # 문자열
print("Apple은 %c로 시작해요" % "A") # 문자

# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("blue", "red"))
print("나는 {0}색과 {1}색을 좋아해요" .format("blue", "red")) # 순서를 정할 수 있음
print("나는 {1}색과 {0}색을 좋아해요" .format("blue", "red")) # 순서를 정할 수 있음

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color = "red"))

# 방법 4 (python v3.6이상)
age = 20 
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")
''' 
# 탈출문자
''' 
# 1. \n : 잘바꿈
print("백문이 불여일견 \n백견이 불여일타")

# 2. \" 또는 \' : 문장 내에서 따옴표
print("저는 '이보슬'입니다.")
print('저는 "이보슬"입니다.')
print("저는 \"이보슬\"입니다.")

# 3. \\ : 문장 내에서 하나의 \ (역슬래시)
print("/Users/elena/PythonWorkspace/practice.py")
print("\\Users\\elena\\PythonWorkspace\\practice.py")

# 4. \r : 커서를 맨 앞으로  이동
print("Red Apple\rPine")
# 5. \t : 탭
print("Red\tApple")
'''

'''
Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오
예) https://naver.com 
규칙1 : https:// 제외 
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수 + "!" 로 구성
생성된 비밀번호 : nav51!
'''
'''
site = "https://youtube.com"
strReplace = site.replace("https://", "") #google.com
print(strReplace)
index = strReplace.find(".") # 6
strSlice = strReplace[0:index] # 0~5
print("{first}{seconds}{third}!" .format(first = strSlice[0:3], seconds = len(strSlice) , third = strSlice.count("e", 0))) 
password = strSlice[0:3] + str(len(strSlice)) + str(strSlice.count("e", 0)) + "!"
print(password)
print("{0}의 비밀번호는 {1} 입니다." .format(site, password))
'''

# 리스트 []
# 지하철 칸별로 10명, 20명, 30명
'''subway1 = 10 
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태우기
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람들을 한 명씩 뒤에서 꺼냄 
print(subway.pop()) # 맨 뒤에 있는 사람(하하)가 출력됨
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬 가능
num_list = [2,3,5,7,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print("순서 뒤집은 결과: ", num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능 
num_list = [1,3,5,6,4]
mix_list = ["조세호", 20, False]
print(mix_list)

# 리스트 확장 
num_list.extend(mix_list) # 두 개의 리스트를 하나의 리스트로 합치는 작업
print(num_list)
'''

# 사전
'''cabinet = {3:"유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

# print(cabinet[5]) # 만약 키값에 5를 넣게 되면 5라는 키는 존재하지 않기 때문에 에러를 뱉는다.
# print(cabinet.get(5)) # get()을 사용하면 키값이 없으면 None이 출력된다. print(cabinet.get(5, "사용가능")) None대체어도 선택 가능

print(3 in cabinet) # True
print(5 in cabinet) # False


cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 키값 업데이트
print(cabinet)
cabinet["A-3"] = "김종국" # 기존에 있던 값 유재석 대신 김종국이 저장된다.
cabinet["C-20"] = "조세호"
print(cabinet)

# 키 삭제
del cabinet["A-3"]
print(cabinet)

# key들만 출력 
print(cabinet.keys())
# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# cabinet 필드 값 초기화
cabinet.clear()
print(cabinet)
'''

# 튜플
'''
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# 튜플은 값을 add 할 수 없음 
# menu.add("생선까스")

# 필드 값을 대입하는 법
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

# 튜플을 통해서 필드 값을 대입하는 법 
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
'''

# 집합 (set)
# 중복 안 됨, 순서 없음(순서는 보장x)
'''
my_set = {1,2,3,3,3} # set는 {}로 되어 있음 !!!
print(my_set)
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # 리스트로 먼저 만든 다음에 set으로 감싼 형태

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 또는 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python) # 김태호, 양세형
print(java.difference(python))

# add (python 할 줄 아는 사람이 늘어남)
python.add("김태호")
print(python)

# remove (java를 까먹음)
java.remove("김태호")
print("자바를 까먹은 김태호를 뺀 결과값 : ",java)
'''

# 자료구조의 변경
# set 자료형으로 생성
'''
menu = {"커피", "우유", "주스"} # 집합(set) 유형임
print(menu, type(menu))

# list 로 변환
menu = list(menu)
print(menu, type(menu))

# tuple 로 변환
menu = tuple(menu)
print(menu, type(menu))
'''

'''
파이썬 대회 주최
댓글 이벤트 진행 
댓글 작성자 추천을 통해서 1명 치킨, 3명은 커피 쿠폰 
조건 1) 댓글은 20명이 작성, 아이디는 1~20
조건 2) 무작위로 추첨하되 중복 불가 
조건 3) random 모듈의 shuffle, sample 활용
'''
# 내가 푼 방법
from random import *
comments = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# 위처럼 일일이 만들지 않아도 됨
comments = list(range(1,21)) # 1~20까지 숫자를 생성
shuffle(comments)
chicken = sample(comments, 1)
tuple = tuple(comments)

# set으로 만든 다음에 차집합을 가지고 온다.
setData1 = set(comments)
setData2 = set(chicken)
comments2 = setData1 - setData2 
coffee = sample(list(comments2), 2)

print('''
--- 담청자 발표 ---
치킨 당첨자 : {0}
커피 당첨자 : {1}
--- 축하합니다 ----
      '''
    .format(chicken, coffee))

