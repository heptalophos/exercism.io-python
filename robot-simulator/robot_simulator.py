# Globals for the directions
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

    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.coordinates = (x, y)

    def turn(self, turn):
        if (turn == 'clockwise'):
            self.direction += 1
        elif (turn == 'counter_clockwise'):
            self.direction -= 1
        else:
            raise Exception('Invalid turn')
        self.direction %= 4

    def turn_right(self):
        self.turn('clockwise')

    def turn_left(self):
        self.turn('counter_clockwise')
     
    def advance(self):
        x, y = self.coordinates
        if self.direction == NORTH:
            self.coordinates = (x, y+1)  
        if self.direction == EAST:            
            self.coordinates = (x+1, y) 
        if self.direction == SOUTH:
            self.coordinates = (x, y-1)  
        if self.direction == WEST:
            self.coordinates = (x-1, y) 
        if self.direction not in [NORTH, EAST, SOUTH, WEST]:
            raise Exception("Invalid bearing")
             

    def move(self, commands):
        for c in commands:
            getattr(self, Robot.valid_commands[c])()