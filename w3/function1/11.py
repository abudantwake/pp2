def pal(word):
    reve = word[::-1]
    if reve == word:
        return True
    else:
        return False

word = input()
print(pal(word))