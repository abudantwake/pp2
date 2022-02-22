def unique(elements):
    newlist = []
    for i in elements:
        if i not in newlist:
            newlist.append(i)
    return newlist

elements = input().split()
print(unique(elements))