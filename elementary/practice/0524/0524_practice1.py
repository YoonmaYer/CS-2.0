num = []
test = int(input("테스트 케이스를 입력하시오: "))
sum = 0

for i in range(test):
    i = int(input("정수를 입력하시오: "))
    num.append(i)

for i in num:
    sum += i

avg = sum/len(num)
print("평균=", avg)