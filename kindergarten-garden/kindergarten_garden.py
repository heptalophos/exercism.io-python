class Garden(object):
    
    CHILDREN = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 
                'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry', 'Samantha', 
                'Patricia', 'Xander', 'Roger']
    
    PLANTS = {p[0]: p for p in ['Clover', 'Grass', 'Radishes', 'Violets']}

    def __init__(self, diagram, students=None):
        self.rows = diagram.split('\n')
        self.students = students or self.CHILDREN
        self.students.sort()

    def plants(self, child):
        i = self.students.index(child)
        plants = [[self.PLANTS[plant] for plant in row] for row in self.rows]
        return sum([row[0 + 2 * i:2 + 2 * i] for row in plants], [])