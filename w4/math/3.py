import math

n=int(input())
a=int(input())

p=(n*a)/2

s=math.sqrt(p*((p-a)**n))

print(s)