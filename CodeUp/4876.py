n = int(input())
result = ['D'] * n  # D를 기본값으로 초기화

for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for j in range(4, 0, -1):  # 4부터 1까지, 두 리스트에서의 개수 카운트
        if a[1:].count(j) != b[1:].count(j):  # index 1부터 slice 적용(index 0은 리스트의 크기)
            result[i] = 'A' if a[1:].count(j) > b[1:].count(j) else 'B'
            break

# 결과 출력
for x in result:
    print(x)
