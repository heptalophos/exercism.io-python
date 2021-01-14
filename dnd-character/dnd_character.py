from random import randint

class Character:

    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()        
        self.hitpoints = 10 + \
                         modifier(self.constitution)

    def ability(self):
        return \
        sum(sorted([randint(1,6) 
                           for x in range (4)])[3:])

def modifier(constitution):
    return (constitution - 10) // 2