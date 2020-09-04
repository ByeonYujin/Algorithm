def sortByHeight(a):
    trees = [i for i in range(len(a)) if a[i] == -1] 
    a = [i for i in a if i != -1]  
    a.sort()
    for i in trees:
        a.insert(i, -1)
    return a
