def append(xs, ys):
    return concat([xs, ys])

def concat(lists):
    return [x for xs in lists for x in xs]

def filter(function, xs):
    return [x for x in xs if function(x)]

def length(xs):
    count = 0
    for x in xs:
        count += 1
    return count

def map(function, xs):
    return [function(x) for x in xs]

def foldl(function, xs, acc):
    for x in xs:
        acc = function(acc, x)
    return acc

def foldr(function, xs, acc):
    return foldl(lambda x, result: 
                 function(result, x), 
                 reverse(xs), 
                 acc)

def reverse(xs):
    return xs[::-1]