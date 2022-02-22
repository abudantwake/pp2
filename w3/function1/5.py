from itertools import permutations

def per():
    string = input()
    permList = permutations(string)

    for x in permList:
        print(''.join(x))

per()