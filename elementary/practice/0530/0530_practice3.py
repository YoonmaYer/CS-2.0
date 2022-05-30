sum = 0

num1 = int(input("첫번째 숫자 입력"))
num2 = int(input("두번째 숫자 입력"))

for x in range(num1, num2 + 1):
    sum += x

print(sum)