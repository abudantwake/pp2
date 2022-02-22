class Shape:
    def __init__(self,l,w):
        self.length = l
        self.wigth = w

class Rectangle(Shape):
    def __init__(self,l,w):
        super().__init__(l,w)

    def area(self):
        return self.length * self.wigth

l = int(input())
w = int(input())
rec = Rectangle(l,w)
print(rec.area())