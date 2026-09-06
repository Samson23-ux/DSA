def searchMatrix(matrix, target):
    row, col = len(matrix) - 1, 0

    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] == target:
            return True
        elif target >= matrix[row][col]:
            col += 1
        else:
            row -= 1
    return False
