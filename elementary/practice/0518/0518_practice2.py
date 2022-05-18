price = []

while 1:
    price.append(int(input("가격을 입력해주세요(0 = 종료) : ")))
    if price[-1] == 0:
        print("종료합니다.")
        break
print(price)
print("위 가격 중 가장 싼 가격은",min(price))