# 1001
print('Hello')

# 1002
print('Hello World')

# 1003
print('Hello\nWorld')

# 1004
print('\'Hello\'')

# 1005
print("\"Hello World\"")

# 1006
print("\"!@#$%^&*()\"")

# 1007
print("\"C:\Download\hello.cpp\"")

# 1008
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

print("\u250C\u252C\u2510")
print("\u251C\u253C\u2524")
print("\u2514\u2534\u2518")

# 1010
n=int(input())
print(n)

# 1011
n=input()
print(n)

# 1012
n=float(input())
print("%f" % n)

# 1013
a, b = map(int, input().split())
print(a, b)

# 1014
a, b = input().split()
print(b, a)

# 1015
n = float(input())
print("%.2f" % n)

# 1017
n=int(input())
print(n, n, n)

# 1018
h, m = input().split(":")
print(h+":"+m)

# 1019
y, m, d = map(int, input().split("."))
print("%04d.%02d.%02d" % (y, m, d))

# 1020
n=input()
print(n.replace('-',''))