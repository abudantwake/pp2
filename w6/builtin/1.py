import math
def pr(list):
    res = math.prod(list)
    return res

list = list(map(int, input().split()))

print(pr(list))
