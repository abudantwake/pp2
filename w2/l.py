l = input()
brackets = []
for x in l:
    if x == "[" or x == "{" or x == "(":
        brackets.append(x)
    else:
        if len(brackets) == 0:
            print("No")
            quit()
        if x == ")" and brackets[-1] == "(":
            brackets.pop(-1)
        if x == "}" and brackets[-1] == "{":
            brackets.pop(-1)
        if x == "]" and brackets[-1] == "[":
            brackets.pop(-1)
if len(brackets) == 0:
    print("Yes")
else:
    print("No")
    #