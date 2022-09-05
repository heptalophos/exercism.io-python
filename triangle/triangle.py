triangle_inequality = lambda f: lambda sides: f(sides) and 2 * max(sides) < sum(sides)

@triangle_inequality
def equilateral(sides):
    return len(set(sides)) == 1

@triangle_inequality
def isosceles(sides):
    return len(set(sides)) <= 2

@triangle_inequality
def scalene(sides):
    return len(set(sides)) == 3
