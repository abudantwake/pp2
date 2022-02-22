def filter_prime(num):
    primes = []
    for i in num:
        if i == 0 or i == 1:
            primes.append(i)
            continue
        pr = True
        for x in range(2, int(int(i) ** 1/2 + 1)):
            if int(i) % x == 0:
                pr = False
                break
        if pr:
            primes.append(i)
    return primes

num = list(map(int,input().split()))
print(filter_prime(num))