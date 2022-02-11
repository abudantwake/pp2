a = int(input())
data = {}
out = []
Max = 0

for x in range(a):
    line = input()
    words = line.split(" ")
    if words[0] in data:
        data[words[0]] += int(words[1])
    else:
        data.update({words[0] : int(words[1])})
    
for x in data:
    if Max < int(data.get(x)):
        Max = int(data.get(x))

for x in data:
    if Max > int(data.get(x)):
        out.append(x + " has to receive " + str(Max - int(data.get(x))) + " tenge")
    else:
        out.append(x + " is lucky!")

out.sort()

for x in out:
    print(x)