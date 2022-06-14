while 1:
    num = int(input("정수를 입력하시오: "))
    if num > 0 :
        for i in range(num):
            print("+")
    elif num < 0:
        for i in range(-num):
            print("-")
    if num == 0:
        break    