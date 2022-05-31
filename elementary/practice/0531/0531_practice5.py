def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x*y
    return z

def divide(x,y):
    z = x/y
    return z
    
while 1:
    num1 = int(input("첫 번째 정수: "))
    num2 = int(input("두 번째 정수: "))
    operator = input("1번(덧셈), 2번(뺄셈), 3번(곱셈), 4번(나눗셈)중 하나를 선택하세요.")
    if operator == '1':
        result=add(num1,num2)
    elif operator == '2':
        result=subtract(num1,num2)
    elif operator == '3':
        result=multiply(num1,num2)
    elif operator == '4':
        result=divide(num1,num2)
    else:
        break
print("결과는 %d입니다." %result)