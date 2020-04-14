class Allergies(object):

    allergies = [ 
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats"
        ]   

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        if self.score & 1 << self.allergies.index(item) >= 1:
            return True
        elif self.score & 1 << self.allergies.index(item) == 0:
            return False
        else:
            return self.score & 1 << self.allergies.index(item)

    @property
    def lst(self):
        return [allergy for allergy in self.allergies
                if self.allergic_to(allergy)]