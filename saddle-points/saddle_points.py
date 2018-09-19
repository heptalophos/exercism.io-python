def saddle_points(matrix):
    if len(matrix) != 0:
        if sum(len(row) for row in matrix) != len(matrix) * len(matrix[0]):
            raise ValueError("irregular matrix")
    return set((ridx, cidx) for ridx, row in enumerate(matrix)
                            for cidx, cell in enumerate(row)
                            if cell == min(list(zip(*matrix))[cidx]) == max(row))
