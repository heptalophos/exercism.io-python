from collections import defaultdict

class School(object):
    def __init__(self):
        self.school = defaultdict(set)
        self.grades = self.school.keys()

    def add_student(self, name, grade):
        self.school[grade].add(name)

    def grade(self, grade):
        return list(sorted(self.school[grade]))

    def roster(self): 
        return [name
                for grade in sorted(self.grades)
                for name in self.grade(grade)]