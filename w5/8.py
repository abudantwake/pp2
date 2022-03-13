import re
def UpperCase(string):
    return re.findall('[A-Z][a-z]*',string)

string = input()
print(UpperCase(string))