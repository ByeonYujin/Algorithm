def isLucky(n):
    li = list(str(n))
    a, b = 0, 0
    for i in range(len(li)//2):
        a += int(li[i])
        b += int(li[len(li)-1-i])
    if a == b:
        return True
    return False
