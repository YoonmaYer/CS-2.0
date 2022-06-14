import random

#함수 선언 부분 : 1부터 46까지의 난수를 생성하여 반환
def getNumber():
    return random.randrange(1,46)
    
#메인 코드
lotto=[]
num=0

while True:
    num=getNumber()
    if lotto.count(num) == 0:
        lotto.append(num)

    if len(lotto)>=6:
        break
    print("추첨된 번호는 ", end = " ")
    for i in range(0,6):
        print("%d" %lotto[i], end='')