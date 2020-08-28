def matrixElementsSum(matrix):
    preRow = list(matrix[0])
    result = sum(preRow)

    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            if preRow[j] != 0:
                result += matrix[i][j]
            else:
                continue
            preRow[j] = matrix[i][j]
            
    return result
