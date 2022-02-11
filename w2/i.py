a = int(input())
shelf = []
taken = []
for x in range(a):
    n = input()
    s = n.split(" ")
    if s[0] == "1":
        shelf.append(s[1])
    else:
        taken.append(shelf[0])
        shelf.pop(0)
for x in taken:
    print(x , end = " ")