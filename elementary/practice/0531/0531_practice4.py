def sum(x,y):
    result=0

    if x>y:
        for i in range(y,x+1):
            result+=i
    else:
        for i in range(x,y+1):
            result+=i
    return result

total = 0


while 1:
    num1 = int(input("첫번째 정수를 입력하세요: "))
    num2 = int(input("두번째 정수를 입력하세요: "))

    total = sum(num1, num2)

    if num1 == num2:
        break
    elif num1 < num2:
        print("%d부터 %d까지의 누적합은 %d입니다." %(num1, num2, total))
    else:
        print("%d부터 %d까지의 누적합은 %d입니다." %(num1, num2, total))