num = int(input("입력하시오: "))
for i in range(1,num+1): # 반복문이 1에서 num+1까지 실행되므로
    for j in range(1,i+1): # i가 1일때 
        print(j, end=" ") # 띄어쓰기 출력
    print()