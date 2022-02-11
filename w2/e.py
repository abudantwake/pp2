l = input()
try:
    num = l.split(" ")

    arr = []
    global out
    for x in range(int(num[0]) - 1):
        arr.append(int(num[1]) + 2*(x+1))
    out = int(num[1])
    for x in arr:
        out ^= x
    print(out)
except:
    a = int(l.strip())
    b = int(input())
    arr = []
    for x in range(a - 1):
        arr.append(b + 2*(x+1))
    out = int(b)
    for x in arr:
        out ^= x
    print(out)