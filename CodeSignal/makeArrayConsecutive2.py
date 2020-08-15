def makeArrayConsecutive2(statues):
    statues.sort()
    size = 0

    for i in range(len(statues) - 1):
        size += statues[i + 1] - statues[i] - 1

    return size

