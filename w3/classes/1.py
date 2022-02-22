class methods:
    def getString(self):
        self.a = input()
        return self.a

    def printString(self):
        print(self.a.upper()) 

line = methods()
line.getString()
line.printString()