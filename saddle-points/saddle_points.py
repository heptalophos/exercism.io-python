def saddle_points(matrix):
    if not matrix:
        return set()
    if any(len(row) != len(matrix[0]) for row in matrix):
            raise ValueError("irregular matrix")
    columns = list(zip(*matrix))
    return {(rx, cx) for rx, row in enumerate(matrix)
                     for cx, col in enumerate(row)
                     if min(columns[cx]) == max(row)}

    # def transpose(m):
    #     return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    # return set((rx, cx) for rx, row in enumerate(matrix)
    #                     for cx, col in enumerate(transpose(matrix))
    #                     if min(col) == max(row))