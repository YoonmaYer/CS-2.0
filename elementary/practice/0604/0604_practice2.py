while 1:
    num1 = int(input("첫번째 정수 :"))
    if num1 == 0:
        break
    num2 = int(input("두번째 정수 :"))
    sel = int(input("계산할 연산번호 선택(1:덧셈 2:곱셈)"))

    if sel == 1:
         print(num1 + num2)
    else:
         print(num1 * num2)