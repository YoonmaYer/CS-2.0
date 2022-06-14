import random

#함수 선언 부분 : 1부터 46까지의 난수를 생성하여 반환
def getNumber():
    return random.randrange(1,46)
    
#메인 코드
lotto=[] # 전역 변수형 리스트 선언
num=0 

while True:
    num=getNumber()
    if lotto.count(num) == 0: # count : 문자열 내부에서 특정 문자 혹은 문자열이 포함되어 있는지 계산해서 반환하는 함수
        lotto.append(num)

    if len(lotto)>=6: # len : 문자열의 길이를 구하는 함수
        break
print("추첨된 번호는 ", end = " ")
for i in range(0,6):
    print("%d" %lotto[i], end=' ')