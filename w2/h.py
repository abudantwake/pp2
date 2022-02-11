l = input()
x_y = l.split(" ")
arr = []
arr2 = []
a = int(input())
for x in range(a):
    pair = input()
    arr.append(pair.split(" "))
for x in arr:
    s = ((int(x[0]) - int(x_y[0]))**2 + (int(x[1]) - int(x_y[1]))**2)**(1/2)
    arr2.append(s)
arr2.sort()
for y in arr2:
    for x in arr:
        if y == ((int(x[0]) - int(x_y[0]))**2 + (int(x[1]) - int(x_y[1]))**2)**(1/2):
            print(x[0] ,x[1])
            arr.remove(x)
            #