# i=1000
# while(i>0):
# 	print(i,end=" ")
# 	print("- 7 =",end=" ")
# 	print(i-7)
# 	i-=7


# li=[]
# while(a>0):
# 	a=int(input())
# 	li.append(a)
# print(li)

num=int(input())
numbers=[]
ans=[]
while (num!=0):
    numbers.append(num)
    num=int(input())
for x in range(int(len(numbers)/2)):
    n=numbers[0] + numbers[-1]
    numbers.pop(0)
    numbers.pop(-1)
    ans.append(n)
if (len(numbers) == 1):
    ans.append(numbers[0])
for x in ans:
    print(x , end = " ")