import re
def find(text):
    pattern = '[A-Z]+[a-z]+'
    return True if re.search(pattern, text) else False

text = input()
print(find(text))