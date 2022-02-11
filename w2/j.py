a = int(input())
disks = []
for x in range(a):
    b = input()
    if b.upper() != b and b.lower() != b and b.isalpha() == False:
        if b not in disks:
            disks.append(b)
print(len(disks))
disks.sort()
for x in disks:
    print(x)