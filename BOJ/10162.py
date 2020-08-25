button = [300, 60, 10]
cookTime = int(input())

if cookTime % button[2] != 0:
    print(-1)
else:
    for i in range(len(button)):
        count = 0
        count += cookTime // button[i]
        cookTime %= button[i]
        print(count, end=" ")