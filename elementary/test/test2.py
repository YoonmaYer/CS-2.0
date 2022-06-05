while 1:
    a = int(input("첫번째 정수 :"))
    b = int(input("두번째 정수 :"))
    num = int(input("계산할 연산번호 선택(1:덧셈 2:곱셈)"))
    if num == 1:
        print(a+b)
    else:
        print(a*b)
    if a == 0:
        break