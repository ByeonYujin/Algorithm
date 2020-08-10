# 1021
import sys

n=sys.stdin.readline()
print(n)

# 1022
n=input()
print(n)

# 1023
n, m=map(int, input().split("."))
print(n)
print(m)

# 1024
n=list(input())
for i in range(len(n)):
    print("\'"+n[i]+"\'")

# 1025
n=list(map(int, input()))
for i in range(len(n)) :
    print("["+str(n[i]*(10**(4-i)))+"]")

# 1026
h, m, s = map(int, (input().split(":")))

print(m)

# 1027
y, m, d = map(int, input().split("."))

print("%02d-%02d-%04d"%(d, m, y))

# 1028
n = int(input())
print(n)

# 1029
n=float(input())
print("%.11lf"%n)

# 1030
n=int(input())
print("%d"%n)

# 1031
n=int(input())
print("%o"%n)

# 1032
n=int(input())
print("%x"%n)

# 1033
n=int(input())
print("%X"%n)

# 1034
n=int(input(), 8)
print(n)

# 1035
n=int(input(), 16)
print("%o"%n)

# 1036
n=input()
print(ord(n))

# 1037
n=int(input())
print(chr(n))

# 1038
n, m = map(int, input().split())
print(n+m)

# 1039
n, m = map(int, input().split())
print(n+m)

# 1040
n=int(input())
print(-n)