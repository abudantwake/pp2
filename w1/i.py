n=int(input())
res=[]
g="@gmail.com"
for i in range(0,n):
	s=input()
	if g in s:
		a=s.strip(g)
		res.append(a)
#print(*res)
print('\n'.join(map(str, res)))