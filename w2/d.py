n=int(input())
for i in range(0,n):
	for j in range(0,n):
		'''print(i,end=",")
		print(j,end=" ")'''
		if(n%2==0):
			if(i>=j):
				print("#",end="")
			else:
				print(".",end="")
		if(n%2!=0):
			if(i>=(n)-j-1):
				print("#",end="")
			else:
				print(".",end="")	
	print()
