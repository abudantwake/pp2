import re
def space(string):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', string)

string = input()
print(space(string))