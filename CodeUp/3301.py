n = int(input())
count = 0
coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in coin:
    count += n // i
    n %= i

print(count)
