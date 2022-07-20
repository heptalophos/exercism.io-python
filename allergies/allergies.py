class Allergies(object):

    allergies = [ 'eggs', 'peanuts', 'shellfish', 
                  'strawberries', 'tomatoes', 
                  'chocolate', 'pollen', 'cats' ]

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        allergen = self.allergies.index(item) 
        return self.score & 1 << allergen >= 1

    @property
    def lst(self):
        return [allergy for allergy in self.allergies
                            if self.allergic_to(allergy)]