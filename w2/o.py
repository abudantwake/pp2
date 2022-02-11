line = input()
num = line.split("+")
n = 0
first = 0
second = 0
for x in range(int(len(num[0])/3)):
    code = num[0][0+n] + num[0][1+n] + num[0][2+n]
    if code == "ONE":
        first += 1 * 10**(len(num[0])/3 - 1 - n/3)
    if code == "TWO":
        first += 2 * 10**(len(num[0])/3 - 1 - n/3)
    if code == "THR":
        first += 3 * 10**(len(num[0])/3 - 1 - n/3)
    if code == "FOU":
        first += 4 * 10**(len(num[0])/3 - 1 - n/3)
    if code == "FIV":
        first += 5 * 10**(len(num[0])/3 - 1 - n/3)
    if code == "SIX":
        first += 6 * 10**(len(num[0])/3 - 1 - n/3)
    if code == "SEV":
        first += 7 * 10**(len(num[0])/3 - 1 - n/3)
    if code == "EIG":
        first += 8 * 10**(len(num[0])/3 - 1 - n/3)
    if code == "NIN":
        first += 9 * 10**(len(num[0])/3 - 1 - n/3)
    if code == "ZER":
        first += 0 * 10**(len(num[0])/3 - 1 - n/3)
    n += 3

n = 0
for x in range(int(len(num[1])/3)):
    code = num[1][0+n] + num[1][1+n] + num[1][2+n]
    if code == "ONE":
        second += 1 * 10**(len(num[1])/3 - 1 - n/3)
    if code == "TWO":
        second += 2 * 10**(len(num[1])/3 - 1 - n/3)
    if code == "THR":
        second += 3 * 10**(len(num[1])/3 - 1 - n/3)
    if code == "FOU":
        second += 4 * 10**(len(num[1])/3 - 1 - n/3)
    if code == "FIV":
        second += 5 * 10**(len(num[1])/3 - 1 - n/3)
    if code == "SIX":
        second += 6 * 10**(len(num[1])/3 - 1 - n/3)
    if code == "SEV":
        second += 7 * 10**(len(num[1])/3 - 1 - n/3)
    if code == "EIG":
        second += 8 * 10**(len(num[1])/3 - 1 - n/3)
    if code == "NIN":
        second += 9 * 10**(len(num[1])/3 - 1 - n/3)
    if code == "ZER":
        second += 0 * 10**(len(num[1])/3 - 1 - n/3)
    n += 3

third = int(first) + int(second)
#print(first , second)
for x in str(third):
    if x == "1":
        print("ONE" , end = "")
    if x == "2":
        print("TWO" , end = "")
    if x == "3":
        print("THR" , end = "")
    if x == "4":
        print("FOU" , end = "")
    if x == "5":
        print("FIV" , end = "")
    if x == "6":
        print("SIX" , end = "")
    if x == "7":
        print("SEV" , end = "")
    if x == "8":
        print("EIG" , end = "")
    if x == "9":
        print("NIN" , end = "")
    if x == "0":
        print("ZER" , end = "")