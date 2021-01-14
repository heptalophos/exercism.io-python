square = lambda n : n * n
sqrt   = lambda n : n ** 0.5
eudist = lambda x, y : \
         sqrt(square(x) + square(y))

def score(x, y):
    distance = eudist(x, y)
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0