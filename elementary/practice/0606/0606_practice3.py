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
item = input("나라를 입력하라")
for k, v in domains.item():
    print(k,": ", v)


