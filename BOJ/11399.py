n = int(input())
time = list(map(int, input().split()))
time.sort()

requiredTime = time[0]
sumOfTime = requiredTime

for i in range(1, n):
    requiredTime = requiredTime + time[i]
    sumOfTime += requiredTime

print(sumOfTime)