class Account():
    owner = ''
    balance = 0
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def show(self):
        return f'Account owner: {self.name} \nAccount balance: {self.balance}' 
    
    def deposit(self, amount):
        self.balance += amount
        return f'Updated balance: {self.balance}'
    
    def withdraw(self, a):
        if self.balance >= a:
            self.balance -= a
            return f'Remaining balance: {self.balance}'    
        return f'The operation cannot be performed!'

ow = input()
bal = int(input())
amount = int(input())
a = int(input())

person = Account(ow,bal)
print(person.show())
print(person.deposit(amount))
print(person.withdraw(a))