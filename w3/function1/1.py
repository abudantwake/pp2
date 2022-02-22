def to_ounces(x):
    return x * 28.3495231

grams = int(input())
ounces = to_ounces(grams)
print(ounces)