def spiral_matrix(size: int) -> [[int]]:
    if size <= 0: return []
    val = 1
    matrix = [[None] * size for _ in range(size)]
    for index in range (size + 1 // 2):
        row = index
        for col in range(row, (size - 1) - row):
            matrix[row][col] = val
            val += 1
        col = index
        for row in range(col, (size - 1) - col):
            matrix[row][size - index - 1] = val
            val += 1
        row = size - index - 1
        for col in range(row, index, -1):
            matrix[row][col] = val
            val += 1
        col = index
        for row in range((size - 1) - col, col, -1):
            matrix[row][col] = val
            val += 1
        row, col = size // 2, (size - 1) // 2
        matrix[row][col] = size * size
    return matrix


