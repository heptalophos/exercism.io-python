def saddle_points(matrix):
    if not matrix:
        return set()
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    columns = list(zip(*matrix))
    return [{"row": rx, "column": cx} 
            for rx, row in enumerate(matrix, 1)
            for cx, col in enumerate(row, 1)
            if min(columns[cx - 1]) == max(row)]