# 파스타 최소 대금
min_pasta = int(input())
for _ in range(2):
    n = int(input())
    min_pasta = min(min_pasta, n)  # 최솟값 찾기

# 생과일 주스 최소 대금
min_juice = int(input())
m = int(input())
min_juice = min(min_juice, m)  # 최솟값 찾기

# 최소 대금 계산
min_price = min_pasta + min_juice
min_price += min_price * 0.1

# 결과 출력
print("%.1f" % min_price)