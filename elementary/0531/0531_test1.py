#phone_book = {}
#phone_book["홍길동"]="010-1234-5678"

#print(phone_book)

phone_book = {"홍길동":"010-1234-5678"}
phone_book["강감찬"] = "010-1234-5679" #key,value
phone_book["이순신"] = "010-1234-5680"

print(phone_book)

for key in sorted(phone_book.keys()):
    print(key,phone_book[key])

items = {"커피음료":7, "펜":3, "종이컵":2, "우유":1, "콜라":4, "책":5}

print("커피음료, 펜, 종이컵, 우유, 콜라, 책의 재고량을 알 수 있습니다.")

name = input("물건의 이름을 입력하시오: ")

if name in items:
    print(items[name])
else:
    print("등록되어 있지 않습니다.")