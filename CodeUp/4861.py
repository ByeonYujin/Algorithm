import math

n, k = map(int, input().split())
r = [[0] * 6 for _ in range(2)]
result = 0

for _ in range(n):
    s, y = map(int, input().split())
    r[s][y - 1] += 1

for i in range(len(r)):
    for j in range(len(r[0])):
        result += math.ceil(r[i][j] / k)

print(result)