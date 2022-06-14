import random

items = { "커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5 }

item = input("물건의 이름을 입력하시오: ")
print(items[item])

english_dict = dict() # 딕셔너리 함수

english_dict['one'] = '하나'
english_dict['two'] = '둘'
english_dict['three'] = '셋'

word = input("단어를 입력하시오: ")
print(english_dict[word])

num = []
sum = 0
t = int(input())

for x in range(t):
    x = int(input("정수를 입력하시오: "))
    num.append(x)

for x in num:
    sum += x

avg = sum / len(num)
print("평균= ", avg)

counters = [0, 0, 0, 0, 0, 0]

for i in range(1000):
    dice = random.randint(0,5)
    counters[dice] = counters[dice] + 1
for i in range(6):
    print("주사위가", i + 1,"인 경우는", counters[i], "번")

contacts = {}

while 1:
    name = input("(입력모드)이름을 입력하시오: ")
    if not name:
        break
    tel = input("전화번호를 입력하시오: ")
    contacts[name] = tel

while 1:
    name = input("(검색모드)이름을 입력하시오: ")
    if not name:
        break
    if name in contacts:
        print(name,"의 전화번호는",contacts[name],"입니다.")
    else:
        print("잘못된 입력입니다.")

domains = { "kr": "대한민국", "sk": "슬로바키아", "no": "노르웨이", "us": "미국", "jp": "일본", "hu": "헝가리", "de": "독일"}

for k, v in domains.items():
    print(k,": ", v)

problems = {'파이썬': '최근에 가장 떠오르는 프로그래밍 언어',
            '변수': '데이터를 저장하는 메모리 공간',
            '함수': '작업을 수행하는 문장들의 집합에 이름을 붙힌것',
            '리스트': '서로 관련이 없는 항목들의 모임'}
for word in problems.keys():
    print("다음은 어떤 단어에 대한 설명일까요?")
    print(problems[word])
    print("(1)파이썬 (2)함수 (3)리스트 (4)변수")
    answer = input("정답(문자만 입력할 것): ")
    if answer == word:
        print("정답입니다!")
    else:
        print("정답이 아닙니다.")