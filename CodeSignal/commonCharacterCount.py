def commonCharacterCount(s1, s2):
    list1, list2 = list(s1), list(s2)
    result = 0
    for x in set(list1):
        if x in list2:
            result += min(list1.count(x), list2.count(x))
    return result
