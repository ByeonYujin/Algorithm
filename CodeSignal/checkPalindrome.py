def checkPalindrome(inputString) :
    strlist = list(inputString)
    for i in range(len(strlist)//2) :
        if (strlist[i] != strlist[len(strlist)-i-1]) :
            return False
        else :
            continue
    return True