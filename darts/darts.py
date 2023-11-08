square = lambda n: n * n
sqrt   = lambda n: n ** 0.5
eudist = lambda x, y: sqrt(square(x) + square(y))

def score(x, y):
    points = 0
    distance = eudist(x, y)
    if distance <= 10:
        points += 1
    if distance <= 5:
        points += 4
    if distance <= 1:
        points += 5
    return points