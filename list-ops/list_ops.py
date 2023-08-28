def foldl(function, xs, acc):
    if not xs:
        return acc
    head, *tail = xs
    return foldl(function, tail, function(acc, head))

def foldr(function, xs, acc):
    if not xs:
        return acc
    head, *tail = xs
    return function(foldr(function, tail, acc), head)

def append(xs, ys):
    return foldr(lambda acc, x: [x] + acc, xs, ys)

def concat(lists):
    return foldl(lambda acc, xs: acc + xs, lists, [])

def length(xs):
    return foldl(lambda acc, _: acc + 1, xs, 0)

def map(function, xs):
    return foldl(lambda acc, x: append(acc, [function(x)]), xs, [])

def filter(function, xs):
    return foldl(lambda acc, x: append(acc, [x]) if function(x) else acc,
                 xs, [])

def reverse(xs):
    return foldr(lambda acc, x: append(acc, [x]), xs, [])