score1 = int(input("국어 성적을 입력하시오: "))
score2 = int(input("수학 성적을 입력하시오: "))
score3 = int(input("영어 성적을 입력하시오: "))
avg = (score1 + score2 + score3) / 3

if avg > 90:
    print("A")
elif avg <= 85 and avg < 90:
    print("B")
elif avg <= 70 and avg < 80:
    print("C")
else:
    print("잘못된 입력입니다.")