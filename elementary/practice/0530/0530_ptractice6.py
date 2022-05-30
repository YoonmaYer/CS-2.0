total = 0
con = 'yes'

while con == 'yes':
    num = int(input())
    total = num + total
    con = input("yes or no")

print(total)