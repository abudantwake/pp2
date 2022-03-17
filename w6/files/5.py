list = ['hello', 'green', 'apple', 'test line']

with open('test1.txt', 'w') as f:
    for i in list:
        f.write('\n' + i)

f.close()