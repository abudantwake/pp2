#num=input()
#print(int(num,2))


num=input()
l=len(num)-1
res=0
def to_dec(bi,cnt):
	global res
	#l=len(num)
	#res=0
	if(cnt==l+1):
		#print(res)
		return res
	res+=int(int(bi[cnt])*(2**(l-cnt)))
'''else:
	res+=2**(l-1)
	l=l-1'''
	return to_dec(bi,cnt+1)
#num=input()
to_dec(num,0)
print(res)