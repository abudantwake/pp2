num=int(input())
a=input()
if a=='k':
	res=num/1024
else:
	res=num*1024
try:
	dec=input()
	b=int(dec)-len(str(ans))+2
	print(str(round(res,int(dec)))+("0"*b))
except:
	print(round(res))