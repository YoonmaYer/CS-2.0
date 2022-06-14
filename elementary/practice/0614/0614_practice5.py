from turtle import ycor


def solve_Problem(x,y):
    sel = int(input("1번(덧셈)과 2번(뺄셈)중 하나를 선택하라:"))
    add = x+y
    min = x-y
    
    if sel == 1:
        print(add)
    else:
        print(min)
    return

solve_Problem(10,10)