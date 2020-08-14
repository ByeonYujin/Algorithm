# 1061
a, b = map(int, input().split())
print(a | b)

# 1062
a, b = map(int, input().split())
print(a ^ b)

# 1063
a, b = map(int, input().split())
result = a>=b and a or b
print(result)

# 1064
a, b, c = map(int, input().split())
result = a if a<=b else b
result = c if result>=c else result
print(result)

# 1065
li = list(map(int, input().split()))
for i in range(len(li)) :
  if (li[i] % 2 == 0) :
    print(li[i])

# 1066
li = list(map(int, input().split()))
for i in range(len(li)) :
  if (li[i] % 2 == 0) :
    print("even")
  else :
    print("odd")

# 1067
n = int(input())
if (n > 0) : {
  print("plus")
}
else : {
  print("minus")
}

if (n % 2) : {
  print("odd")
}
else : {
  print("even")
}

# 1068
n = int(input())
if (n >= 90) :
  score = 'A'
elif (n >= 70) :
  score = 'B'
elif (n >= 40) :
  score = 'C'
else :
  score = 'D'
print(score)

# 1069
n = input()
def f(x) :
  return {
    'A' : 'best!!!',
    'B' : 'good!!',
    'C' : 'run!',
    'D' : 'slowly~'
  }.get(x, 'what?')
print(f(n))

# 1070
n = int(input())

if 3<=n<=5 :
  result="spring"
elif 6<=n<=8 :
  result="summer"
elif 9<=n<=11 :
  result="fall"
else :
  result="winter"

print(result)

# 1071
data = list(map(int, input().split()))
i=0
while(data[i]!=0 and i<len(data)):
  print(data[i])
  i+=1

# 1072
size = int(input())
a = input().split()
for x in a :
  print(x)

# 1073
list = list(map(int, input().split()))

i=0
while(list[i]) :
  print(list[i])
  i+=1

# 1074
n = int(input())
for i in range(n, 0, -1) :
  print(i)

# 1075
n = int(input())
for i in range(n-1, -1, -1) :
  print(i)

# 1076
n = input()

for i in range(ord('a'), ord(n)+1) :
  print(chr(i), end=" ")

# 1077
n = int(input())
for i in range(n+1) :
  print(i)

# 1078
n = int(input())
result = 0
for i in range(1, n+1) :
  if i % 2 == 0 :
    result += i
print(result)

# 1079
list = list(input().split())
i = 0

while(i<len(list)) :
  print(list[i])
  if (list[i] == 'q') :
    break;
  i+=1

# 1080
n = int(input())

i, sum = 1, 0
while(sum < n) :
  sum += i
  i += 1

print(i-1)
