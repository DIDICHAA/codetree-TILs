n, m = tuple(map(int, input().split()))

def ans(n, m):
    res = 0
    for i in range(1, min(n, m)+1):
        if n % i == 0 and m % i == 0:
            res = i

    print(res)

ans(n, m)