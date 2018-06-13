from collections import defaultdict

class School(object):
    def __init__(self, name):
        self.db = defaultdict(set)
        self.school_name = name

    def add(self, name, grade):
        self.db[grade].add(name)

    def grade(self, grade):
        return self.db[grade]

    def sort(self):
        return ((grade, tuple(sorted(names))) for grade, names in sorted(self.db.items()))
