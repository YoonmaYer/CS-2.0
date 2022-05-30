number = int(input("입력이 0이면 종료됩니다. 정수를 입력하세요: "))
max = number

while number != 0:
    number = int(input("입력이 0이면 종료됩니다. 정수를 입력하시오: "))
    if number > max:
        max = number

print("최댓값은 %d입니다."%max)