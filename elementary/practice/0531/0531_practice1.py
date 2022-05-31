count = 1
sum1 = 0
sum2 = 0

while count <= 5:
    print("5개의 수를 입력받습니다. 정수",count, "를 입력하세요:")
    num = int(input())
    count +=1
    if num % 2 == 0:
        sum1 += num
    else:
        sum2 += num
print(sum1,sum2)