l = input()
dates = []
while l!="0":
    dmy = l.split(" ")
    dcheck = dmy[2] + " " + dmy[1] + " " + dmy[0]
    dates.append(dcheck)
    l = input()
dates.sort()
for x in dates:
    new = x.split(" ")
    print(new[2] , new[1] , new[0])