# 19*19 배열 초기화(모든 값 0)
arr = [[0]*19 for _ in range(19)]

# 바둑판 상황 입력받기
for i in range(19) :
  arr[i] = list(map(int, input().split()))

# 십자 뒤집기 횟수 입력받기
n = int(input())

for i in range(n) :
  # 십자 뒤집기 횟수(n)만큼 좌표 입력받기
  x, y = map(int, input().split())

  # 십자 뒤집기 -> 입력받은 좌표의 행(x), 열(y)에 있는 원소들의 값이 0이면 1, 1이면 0으로 변경
  for j in range(19) :
    if (arr[x-1][j] == 0) :
      arr[x-1][j] = 1
    else :
      arr[x-1][j] = 0
    if (arr[j][y-1] == 0) :
      arr[j][y-1] = 1
    else :
      arr[j][y-1] = 0

# 결과 출력
for i in range(19) :
  for j in range(19) :
    print(arr[i][j], end=" ")
  print()