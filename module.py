# # 모듈 사용
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러갔을 때 가격 
# theater_module.price_morning(4) # 4명이서 조조할인 영화 보러 갔을 때 가격
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러갔을 때 가격

# # 모듈 import 할 때 별칭을 사용할 수도 있음
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)


# # 모듈 import 할 때 from을 사용하면 앞에 모듈명을 작성할 필요없이 함수만 작성해주면 됨
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning 
# price(5)
# price_morning(4)
# price_soldier(7) # 이 경우는 위에서 import를 안 해줬기 때문에 오류 남


# as를 통해서 명칭을 설정할 수도 있음
# from theater_module import price_soldier as price 


# 여행 패키지 
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail() 

# # import * 했을 때 __init__ 파일에 공개 범위를 지정해줘야 하는데 지정을 안해서 오류가 나는 거임
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# thailand_trip = thailand.ThailandPackage()
# thailand_trip.detail()

# from travel import *
# import inspect 
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 내장함수
# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요? ")
# print("{0}은 아주 좋은 언어입니다.".format(language))

# # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())

# import random
# print(dir(random))

# list = [1,2,3]
# print(dir(list))

# name = "dir"
# print(dir(name))

# # 외장함수
# # 내장함수와 다르게 직접 import를 해준다음에 사용 가능
# import os
# print(os.getcwd()) # 현재 디렉토리
# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# 날짜 관련 함수
import time
import datetime
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장


from byme import *
sign()