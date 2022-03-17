with open('test.txt', 'r') as f:
    num = sum(1 for f.readline in f)
    print(num)


f.close()