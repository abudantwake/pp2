def l_up(string):
    u =  sum(1 for x in string if x.isupper())
    l = sum(1 for x in string if x.islower())
    return u, l


string = input()
print(l_up(string))