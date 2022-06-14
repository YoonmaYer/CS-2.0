def print_address(name):
    print("서울특별시 종로구 1번지")
    print("파이썬 빌딩 7층")
    print(name)

print_address("홍길동")

def calculate_area(radius):
    area = 3.14 * radius**2
    return area

c_area = calculate_area(5.0)

print(calculate_area(5.0))

area_sum = calculate_area(5.0) + calculate_area(10.0)
print(calculate_area(10.0))

def calculate_area():
    area = 3.14 * r**2
    return area

r = float(input("원의 반지름: "))
area = calculate_area()
print(area)

def calculate_area (radius):
    global area
    area = 3.14 * radius **2 # 전역변수 area에 계산 값을 저장하려고 한다.
    return

area = 0
r = float(input("원의 반지름: "))
calculate_area(r)
print(area)

def get_sum(start,end):
    sum = 0
    for i in range(start,end+1):
        sum += i
    return sum

print(get_sum(1,10)) #누적합

def greet(name, msg):
    print("안녕", name + ',' +msg)

greet("철수","좋은 아침!")

def greet(name, msg="별일 없죠?"):
    print("안녕", name + ',' +msg)

greet("영희")

def calc(x,y,z):
    return x+y+z

print(calc(10,20,30))

print(calc(x=10,y=20,z=30))

print(calc(y=20, x=10, z=30))

print(calc(10,y=20,z=30))