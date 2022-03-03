# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

n=input()

#def num(n):
  #s=1
  for i in range(1,n):
    yield i**2
    print(i)

x=(num(n))

#<generator object f_gen at 0x0000023EE468D6D0>

#for i in x:
# print(i)