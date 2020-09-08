import math

x, y, z = map(int, input().split())

secKey = math.gcd(math.gcd(x, y), z)
print(secKey)