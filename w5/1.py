import re
def f(text):
    pattern = '^a(b*)$'
    return True if re.search(pattern, text) else False

text = input()
print(f(text))