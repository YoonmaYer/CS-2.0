num = []
print("3개의 가격을 입력해주세요")
num.append(int(input("가격을 입력해주세요 : ")))
num.append(int(input("가격을 입력해주세요 : ")))
num.append(int(input("가격을 입력해주세요 : ")))
print(num)
print("위 가격 중에서 가장 싼 가격은" ,min(num))