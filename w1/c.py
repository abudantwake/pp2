s=input()
cnt=0
for i in s:
	if(ord(i)>=65 and ord(i)<=90):
		l=chr(ord(i)+32)
		s=s.replace(i,l)
print(s)