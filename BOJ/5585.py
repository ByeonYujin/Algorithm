n = int(input())
m = 1000 - n
count = 0
coin = [500, 100, 50, 10, 5, 1]
for i in coin:
    count += m // i
    m %= i
print(count)
