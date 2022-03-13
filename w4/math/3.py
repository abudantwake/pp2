import math

n=int(input())
a=int(input())

p=(n*a)/2
d=(p-a)**n

s=math.sqrt(p*((p-a)**n))

print(s)