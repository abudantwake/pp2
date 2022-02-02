s=input() 
t=input() 
res=""
f=s.find(t)
if (not(f==-1)):
    res+=str(f)
l=s.rfind(t) 
if (not(l==f) and l!=-1):
    res+=" "
    res+=str(l)
if len(res)!=0:
    print (res)