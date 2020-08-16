# 1081
n, m = map(int, input().split())

for i in range(1, n+1) :
  for j in range(1, m+1) :
    print(i, j)

# 1082
n = int(input(), 16)

for i in range(1, 16) :
  print("%0X*%0X=%0X" % (n, i, i*n))

# 1083
n = int(input())

for i in range(1, n+1) :
  if (i%3==0) :
    print('X')
  else :
    print(i)

# 1084
r, g, b = input().split()
sum = 0
R, G, B = int(r), int(g), int(b)

for i in range(R) :
  for j in range(G) :
    for k in range(B) :
      print("%d %d %d"%(i, j, k))
      sum+=1
print(sum)

# 1085
h, b, c, s = map(int, input().split())

bit = h*b*c*s
byte = bit/8
kbyte = byte/1024
mbyte = kbyte/1024

print("%.1f MB" % mbyte)

# 1086
w, h, b = map(int, input().split())

bit = w*h*b
byte = bit/8
kbyte = byte/1024
mbyte = kbyte/1024

print("%.2f MB" % mbyte)

# 1087
n = int(input())

i, sum = 0, 0
while (sum < n) :
  sum += i
  i += 1

print(sum)

# 1088
n = int(input())

for i in range(n+1) :
  if (i%3 != 0) :
    print(i, end=" ")
  else :
    continue;

# 1089
a, d, n = map(int, input().split())
print("%d"%(a+(n-1)*d))

# 1090
a, r, n = map(int, input().split())
print(a*(r**(n-1)))

# 1091
a, m, d, n = map(int, input().split())

for _ in range(n-1) :
  a = a*m + d

print(a)

# 1092
import math

a, b, c = map(int, input().split())

def lcm(x, y) :
  gcd = math.gcd(x, y)
  return (x*y // gcd)

print(lcm(lcm(a, b),c))

# 1093
a = int(input())
num = list(map(int, input().split()))
arr = [0]*23

for i in num :
  arr[i-1] += 1

for i in range(len(arr)) :
  print(arr[i], end=" ")

# 1094
a = int(input())
num = list(map(int, input().split()))

for i in range(len(num)-1, -1, -1) :
  print(num[i], end=" ")

# 1095
a = int(input())
num = list(map(int, input().split()))
num.sort()
print(num[0])

# 1096
a = int(input())
arr = [[0]*19 for _ in range(19)]

for i in range(a) :
  x, y = map(int, input().split())
  arr[x-1][y-1] = 1

for i in range(19) :
  for j in range(19) :
    print(arr[i][j], end=" ")
  print()

