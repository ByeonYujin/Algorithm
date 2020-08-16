# 행, 열 수 입력받고 격자판 배열 초기화
h, w = map(int, input().split())
arr = [[0]*w for _ in range(h)]

# 입력받은 막대 수만큼 막대 정보 입력받기
n = int(input())

for _ in range(n) :
  l, d, x, y = map(int, input().split())

  # 막대 수 길이만큼 칸 채우기
  for i in range(l) :
    if d == 0 :
      arr[x-1][y-1+i] = 1
    else :
      arr[x-1+i][y-1] = 1

# 출력
for i in range(h) :
  for j in range(w) :
    print(arr[i][j], end=' ')
  print()