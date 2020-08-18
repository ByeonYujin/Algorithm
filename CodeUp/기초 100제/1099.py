# 미로상자 초기화
box = [[0] * 10 for _ in range(10)]
for i in range(10):
    box[i] = list(map(int, input().split()))

# 시작 위치
x, y = 1, 1

while box[x][y] != 2 and x < 9 and y < 9:
    box[x][y] = 9  # 거쳐간 곳은 값을 9로 바꾼다

    if box[x][y + 1] != 1:  # 오른쪽으로 이동할 수 있으면
        y += 1  # 오른쪽으로 이동
    elif box[x + 1][y] != 1:  # 아래로 이동할 수 있으면
        x += 1  # 아래로 이동
    else:  # 더이상 이동 불가
        break

# 현재 위치 값을 9로 바꾼다
box[x][y] = 9

# 결과 출력
for i in range(10):
    for j in range(10):
        print(box[i][j], end=' ')
    print()