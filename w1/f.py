n=int(input())
arr=[]
for i in range(0,n):
	arr=(input())
for i in range(0,len(arr)):
	#if(int(arr[i])<=10):
	#	print("Go to work!")
	#	break
	#el
	if(int(arr[i])>10 and int(arr[i])<=25):
		print("You are weak")
	else:
	#(int(arr[i])>25 and int(arr[i])<=45):
		print("Okay, fine")
	#else:
	#	print("Burn! Burn! Burn Young!")