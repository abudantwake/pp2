def jumpy(num):
	maxi=0
	i=0
	for i in range(len(num)):
		if(i>maxi):
			break
		maxi=max(int(num[i])+i,maxi)
	if(maxi>=len(num)-1):
		return 1
	return 0
print(jumpy(input().split()))