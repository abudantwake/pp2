import re
def seq(text):
    pattern = '^[a-z]+_[a-z]+'
    return True if re.search(pattern, text) else False

text = input()
print(seq(text))