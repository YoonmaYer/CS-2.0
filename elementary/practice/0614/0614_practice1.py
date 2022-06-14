def calculate_area(radius):
    global result
    result = 3.14 * radius ** 2 #result = 지역변수, 함수 안에서만 사용 가능
    return 

r = float(input("원의 반지름: ")) #r = 전역변수, 함수 외부에서 생성, 어디서나 사용 가능
area = calculate_area(r)
print(result)