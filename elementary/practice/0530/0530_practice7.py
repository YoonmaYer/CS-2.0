import random

while 1:
    x = random.randint(1,100)
    y = random.randint(1,100)
    print(x,"+",y,"= ",end="")
    answer = int(input())
    if answer == x+y:
        print("right")
    else:
        print("noob")
    end = input("그만두려면 f를 눌러")
    if end == 'f':
        break

