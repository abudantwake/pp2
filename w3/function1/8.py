def has_007(nums):
    c1 = False ; c2 = False

    for i in nums:
        if c1 == False and i == 0:
            c1 = True
        if c1 == True and c2 == False and i == 0:
            c2 = True
        if c2 == True and i == 7:
            return True

    return False

nums = list(map(int,input().split()))
print(has_007(nums))