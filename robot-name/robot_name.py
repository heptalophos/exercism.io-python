from random import choice as rc
from string import ascii_uppercase as ls, digits as ds

class Robot(object):

    assigned_names = set()

    def __init__(self):
        self.name = None
        self.reset()

    def reset(self):
        self.name = self.generate_name()
        while self.name in self.assigned_names:
            self.name = self.generate_name()
        self.assigned_names.add(self.name)

    def generate_name(self):
        alphas = 2 * rc(ls)
        numeric = 3 * rc(ds)
        return alphas + numeric 
