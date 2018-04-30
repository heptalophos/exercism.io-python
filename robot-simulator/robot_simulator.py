# Globals for the bearings
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot(object):
    
    valid_commands = {
        'R': 'turn_right',
        'L': 'turn_left',
        'A': 'advance',
    }

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def turn_right(self):
        self.bearing += 1
        self.bearing %= 4

    def turn_left(self):
        self.bearing -= 1
        self.bearing %= 4
     
    def advance(self):
        x, y = self.coordinates
        if self.bearing == NORTH:
            self.coordinates = (x, y+1)
        elif self.bearing == EAST:
            self.coordinates = (x+1, y)
        elif self.bearing == SOUTH:
            self.coordinates = (x, y-1)
        elif self.bearing == WEST:
            self.coordinates = (x-1, y)
        else:
            raise Exeption("Invalid direction") 

    def simulate(self, commands):
        for c in commands:
            getattr(self, Robot.valid_commands[c])()