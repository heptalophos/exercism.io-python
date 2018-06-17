MERCURY = 0.2408467
VENUS   = 0.61519726
EARTH   = 1.0
MARS    = 1.8808158
JUPITER = 11.862615
SATURN  = 29.447498
URANUS  = 84.016846
NEPTUNE = 164.79132

class SpaceAge(object):
    
    EARTH_YEAR = 31557600

    def __init__(self, seconds):
        self.seconds = seconds
        self.on_earth   = self.on_planet(EARTH)
        self.on_mercury = self.on_planet(MERCURY)
        self.on_venus   = self.on_planet(VENUS)
        self.on_mars    = self.on_planet(MARS)
        self.on_jupiter = self.on_planet(JUPITER)
        self.on_saturn  = self.on_planet(SATURN)
        self.on_uranus  = self.on_planet(URANUS)
        self.on_neptune = self.on_planet(NEPTUNE)

    def on_planet(self, local_year):
        def inner():
            return round(self.seconds / (self.EARTH_YEAR * local_year), 2)
        return inner
    

