s = input()
s = list(s.lower())
max, r = 0, ""

for x in set(s):
  if s.count(x) > max:
    max = s.count(x)
    r = x.upper()
  elif s.count(x) == max:
    r = '?'

print(r)
