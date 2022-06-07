import random

num = random.randint(1,100)

if num % 2 == 0 and num % 3 == 0:
    print(num,"은 2와 3으로 나누어떨어지지 않습니다")
else:
    print("error")