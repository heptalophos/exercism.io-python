triangle_inequality = lambda sides: 2 * max(sides) < sum(sides)

def equilateral(sides):
    return len(set(sides)) == 1 and triangle_inequality(sides)

def isosceles(sides):
    return len(set(sides)) <= 2 and triangle_inequality(sides)

def scalene(sides):
    return len(set(sides)) == 3 and triangle_inequality(sides)
