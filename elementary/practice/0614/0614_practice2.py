def sum(x,y):
    result = 0
    if x > y:
        for i in range(y,x+1):
            result += i
    else:
        for i in range(x,y+1):
            result += i
    return result

total = 0

num1 = int(input())
num2 = int(input())

total = sum(num1, num2)

if num1 > num2:
    print(total)
else:
    print(total)