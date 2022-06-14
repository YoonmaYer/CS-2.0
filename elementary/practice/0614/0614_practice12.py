sum = 0

for i in range(101):
	sum +=i

	if sum >= 1000 :
		print("합이 1000을 넘을 때의 합의 값 : ", sum)
		print("합이 1000을 넘게 만든 수 : ", i)
		break