l=input()
global newline
for i in l:
    if (i.isalpha() == False and i.isspace() == False):
        l=l.replace(i , "")
w = l.split(" ")
w = list(set(words))
w.sort()
print(len(w))
for x in w:
    print(x)
    #