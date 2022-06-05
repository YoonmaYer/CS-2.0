import random

score = random.randint(0,100)

if score > 90:
    print(score,"점은 장학생이다")
elif score > 60:
    print(score,"점은 합격이다")
elif score < 60:
    print(score,"점은 불합격이다")
else:
    print("넌 뭐냐?") 