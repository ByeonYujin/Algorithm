def almostIncreasingSequence(sequence):
    count, i = 0, 0

    while i < len(sequence) - 1 and len(sequence) > 2:
        if sequence[i] >= sequence[i + 1]:
            count += 1
            if i != 0:
                if sequence[i - 1] < sequence[i + 1]:
                    sequence[i] = sequence[i - 1]
                else:
                    sequence[i + 1] = sequence[i]

        i += 1

        if count >= 2:
            return False

    return True