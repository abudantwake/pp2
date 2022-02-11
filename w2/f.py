a = int(input())
data = {}
out = []
maxi = 0
for x in range(a):
    line = input()
    w = l.split(" ")
    if w[0] in data:
        data[w[0]] += int(w[1])
    else:
        data.update({w[0] : int(w[1])})
for x in data:
    if maxi < int(data.get(x)):
        maxi = int(data.get(x))
for x in data:
    if maxi > int(data.get(x)):
        out.append(x + " has to receive " + str(maxi - int(data.get(x))) + " tenge")
    else:
        out.append(x + " is lucky!")
out.sort()
for x in out:
    print(x)