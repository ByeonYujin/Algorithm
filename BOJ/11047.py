n, k = map(int, input().split())

coin = [0] * n
for i in range(n):
    coin[i] = int(input())
coin.sort(reverse=True)

result = 0
for x in coin:
    result += k//x
    k %= x

print(result)
