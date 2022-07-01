class School(object):
    def __init__(self):
        self.school   = {}
        self.enrolled = []

    def add_student(self, name, grade):
        if name in self.roster():
            self.enrolled.append(False)
        else:
            if not grade in self.school.keys():
                self.school[grade] = []
            self.school[grade].append(name)
            self.enrolled.append(True)

    def grade(self, grade):
        return sorted(self.school.get(grade, []))

    def roster(self): 
        roster = []
        if len(self.school.keys()) > 0:
            grades = [g for (g, _) in sorted(self.school.items())]
            for grade in grades:
                students = [s for s in sorted(self.school[grade])]
                roster.extend(students)
        return roster

    def added(self):
        return self.enrolled