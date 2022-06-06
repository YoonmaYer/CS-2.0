def happyBirthday(name):
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday, dear",name)
    print("Happy birthday to you!")

happyBirthday("홍길동")

def number():
    x = int(input("첫 번째 정수: "))
    y = int(input("두 번째 정수: "))
    z = x + y
    return print("정수", x,"+",y,"의 합은",z,"입니다.")

number()

# 원의 면적 = r ** 2 * PI
# 원의 둘레 = r * 2 * PI
def circleArea(radius):
    return radius ** 2 * PI

def circleCircumference(radius):
    return radius * 2 * PI

PI = 3.14
print("반지름이 5인 원의 면적: ",circleArea(5))
print("반지름이 5인 원의 둘레: ",circleCircumference(5))

def add(a,b):
    return a + b
def min(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

a = int(input())
b = int(input())
print(add(a,b))
print(min(a,b))
print(mul(a,b))
print(div(a,b))