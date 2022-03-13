import re
def r(text):
    return re.sub('[ ,.]', ':', text)

text = input()
print(r(text))