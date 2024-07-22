import math

n, m = tuple(map(int, input().split()))

def lcm(n, m):
    return n * m // math.gcd(n, m)

result = lcm(n, m)
print(result)