#함수 선언 부분
def multi(v1,v2):
    retList=[]
    res1=v1+v2
    res2=v1-v2
    retList.append(res1)
    retList.append(res2)
    return retList

myList=[]
hap, sup = 0,0

myList=multi(100,200)
hap=myList[0]
sub=myList[1]

print("합은 %d이고 차는 %d이다" %(hap,sub))