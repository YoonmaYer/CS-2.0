def menu():
    print("1번을 입력하면 : 섭씨 온도를 화씨 온도로")
    print("종료하려면 1번을 제외한 값을 입력하세요")
    sel=int(input("번호 선택 : "))
    return sel

def input_c() :
    c=float(input("섭씨  온도를  입력하세요")) 
    return c

def ctof(c) :
    temp=c*9.0/5.0+32
    return temp

while True:
    index=menu()
    if index==1 :
        t=input_c()
        t2=ctof(t)
        print("화씨  온도는  %d"%t2) 
    else:
        break