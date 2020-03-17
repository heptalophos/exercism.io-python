from collections import defaultdict

class School(object):
    
    def __init__(self):
        self.school = defaultdict(set)
        
    def add_student(self, name, grade):
        self.school[grade].add(name)
        
    def grade(self, grade):
        return list(sorted(self.school[grade]))

    def roster(self): 
        grades = self.school.keys()
        return [name
                for grade in sorted(grades)
                for name in self.grade(grade)]