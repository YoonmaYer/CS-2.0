total = 0

while 1:
    num = int(input("입력이 0이면 종료됩니다. 정수를 입력하세요: "))
    total += num
    if num == 0:
        break
print(total)