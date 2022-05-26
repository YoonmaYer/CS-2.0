print("선택한 번호의 넓이를 구하시오.")
choice = int(input("선택하시오(1:사각형 2:삼각형)"))
num1 = int(input("가로를 입력하시오: "))
num2 = int(input("세로를 입력하시오: "))

if choice == 1:
    square = num1 * num2
    print("넓이는 ", square, "입니다.")
elif choice == 2:
    triangle = num1 * num2 / 2
    print("넓이는", triangle, "입니다.")
else:
    print("잘못된 입력입니다.")