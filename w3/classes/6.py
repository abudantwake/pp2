def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, n //2):
        if n % i == 0:
            return False
    return True

a = list(map(int,input().split()))
print(list(filter(lambda x: is_prime(x), a)))