def transpose(lines):
    if not lines:
        return ''
    matrix = []
    for row, line in enumerate(lines.splitlines()):
        for col, ch in enumerate(line):
            while len(matrix) <= col:
                matrix.append([])
            while len(matrix[col]) < row:
                matrix[col].append(' ')
            matrix[col].append(ch)
    return '\n'.join(''.join(r) for r in matrix)
