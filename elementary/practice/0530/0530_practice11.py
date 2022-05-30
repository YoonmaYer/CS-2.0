count = 1
sum = 0

while count <= 5:
    print("5개의 수를 입력받습니다. 정수",count, "를 입력하세요:")
    num = int(input())
    count +=1
    if num % 2 == 0:
        sum += num
print(sum)