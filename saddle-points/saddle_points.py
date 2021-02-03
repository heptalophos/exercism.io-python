def saddle_points(matrix):
    if not matrix:
        return set()
    if any(len(row) != len(matrix[0]) for row in matrix):
            raise ValueError("irregular matrix")
    columns = list(zip(*matrix))
    return [{"row": rx + 1, "column": cx + 1} 
            for rx, row in enumerate(matrix)
            for cx, col in enumerate(row)
            if min(columns[cx]) == max(row)]
