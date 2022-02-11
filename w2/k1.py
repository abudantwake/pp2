line = input()
global newline
for i in line:
    if i.isalpha() == False and i.isspace() == False:
        line = line.replace(i , "")
words = line.split(" ")
word = list(set(words))
word.sort()
print(len(word))
for x in word:
    print(x)
    #