a = int(input())
arr = []

l = input()
num = l.split(" ")
num2 = num.copy()
maxi = 0 

for x in num:
    
    num2.remove(x)
    for y in num2:
        if int(x) * int(y) > maxi:
            maxi = int(x) * int(y)

print(maxi)
#