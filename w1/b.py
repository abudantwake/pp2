word=input()
l=int(len(word))
sum=0
for i in range(0,l):
	sum+=int(ord(word[i]))
if sum<300:
	print("Oh, no!")
else:
	print("It is tasty!")