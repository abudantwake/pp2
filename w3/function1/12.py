def histogram(l):
    for i in l:
        for x in range(int(i)):
            print('*',end = " ")
        print(" ")

a = list(map(int,input().split()))
histogram(a)