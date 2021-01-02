class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(val) 
                        for val in 
                        row.split(' ')] 
                        for row in 
                        matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index - 1][:]

    def column(self, index):
        return [rows[index - 1] 
                for rows in self.matrix]
