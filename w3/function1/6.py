def rev(line):
    string = []
    for x in line:
        string.insert(0, x)
    print(" ".join(string))

line = input().split()
rev(line)