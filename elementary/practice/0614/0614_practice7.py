def add(x,y):
    z = x + y
    return z

def min(x,y):
    z = x-y
    return z
def mul(x,y):
    z = x*y
    return z

def div(x,y):
    z = x/y
    return z
num1 = int(input())
num2 = int(input())

sel = int(input("1. plus 2. minus 3.mul 4.div"))

if sel == 1:
    result = add(num1,num2)
elif sel == 2:
    result = min(num1,num2)
elif sel == 3:
    result = mul(num1,num2)
elif sel == 4:    
    result = div(num1,num2)
else:
    print("error")   

print(result) 