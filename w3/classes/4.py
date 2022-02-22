import math

class PointClass():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        return (self.x, self.y)

    def move(self,x,y):
        self.x += x
        self.y += y

    def dist(self,l,m):
        x1 = l - self.x
        y1 = m - self.y
        return math.sqrt(x1 ** 2 + y1 ** 2)

x = int(input())
y = int(input())
s = PointClass(x,y)
q = int(input())
w = int(input())
r = s.move(q,w)
print(s.show())
l = int(input())
m = int(input())
print(s.dist(l,m))