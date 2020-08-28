def allLongestStrings(inputArray):
    maxLen = max(len(x) for x in inputArray)
    longestStrings = list(x for x in inputArray if len(x) == maxLen)
    return longestStrings
