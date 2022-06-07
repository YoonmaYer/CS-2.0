ary1 = []
ary2 = []

ary1 = list(map(int,input("정수값 4개 입력: ").split( )))

for i in range(3,-1,-1):
    ary2.append(ary1[i])
for ary in ary1:
    print(ary, end = ' ')
    

print(ary2)