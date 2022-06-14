def myFunc(a,b=0,c=0) : 
    ret=a+b+c
    return ret
print("매개변수가 1개로 호출  =" ,myFunc(1))
print("매개변수가 2개로 호출  =" ,myFunc(1,2))
print("매개변수가 3개로 호출 =" ,myFunc(1,2,3))