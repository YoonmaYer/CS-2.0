import random

def math(x,y):
    print(x, "+", y)
    return x + y
    
num1 = random.randint(1,100)
num2 = random.randint(1,100)
result = num1 + num2

while 1:
    print("정수의 합을 구하시오")
    math(num1,num2)
    final = int(input())
    if result == final:
        print("굿")
        break
    else:
        print("다시")
    

