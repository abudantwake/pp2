d,c=map(int,input().split())
prime=True
if(d>1):
	for i in range(2,d//2+1):
		if(d%i==0):
			prime=False
			break
else:
	prime=False
if(d<500 and prime and c%2==0):
	print("Good job!")
else: 
	print("Try next time!")