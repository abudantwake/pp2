#num=input()
#print(int(num,2))
def to_dec(num):
	l=len(num)
	res=0
	if(l<0):
		#print(res)
		return res
	else:
		res+=2**(l-1)
		l=l-1
	return to_dec
num=input()
print(to_dec(num))