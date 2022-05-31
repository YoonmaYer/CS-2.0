while 1:
    dan=int(input("원하는 단을 입력하세요:"))
    i=1
    if dan == 0:
        break
    while i<=9:
        print("%d*%d=%d" %(dan,i,dan*i))
        i=i+1