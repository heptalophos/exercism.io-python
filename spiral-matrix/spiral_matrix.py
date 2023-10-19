def spiral_matrix(size: int) -> [[int]]:
    if not size: return []
    matrix = [[None for _ in range(size)] for _ in range(size)]
    val = 1
    for idx in range (size + 1 // 2):
        for col in range(idx, (size - 1) - idx, 1):
            row = idx
            matrix[row][col] = val
            val += 1
        for row in range(idx, (size - 1) - idx, 1):
            col = (size - 1) - idx
            matrix[row][col] = val
            val += 1
        for col in range((size - 1) - idx, idx, -1):
            row = (size - 1) - idx
            matrix[row][col] = val
            val += 1
        for row in range((size - 1) - idx, idx, -1):
            col = idx
            matrix[row][col] = val
            val += 1
        row, col = size // 2, (size - 1) // 2
        matrix[row][col] = size * size
    return matrix


