num1 = int(input("첫 번째 정수를 입력하시오: "))
num2 = int(input("두 번째 정수를 입력하시오: "))
sum = 0

for x in range(num1, num2+1):
    sum += x
print("%d부터 %d까지의 누적 합은 %d입니다"%(num1,num2,sum))