score1 = int(input("국어 성적을 입력하시오: "))
score2 = int(input("수학 성적을 입력하시오: "))
score3 = int(input("영어 성적을 입력하시오: "))
avg = (score1 + score2 + score3) / 3
result = score1 + score2 + score3

print("세 과목의 총합은 %d 이고, 평균은 %1f입니다."%(result,avg))