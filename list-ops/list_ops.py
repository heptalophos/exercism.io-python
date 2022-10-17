def append(xs, ys):
    return foldr(lambda x, acc: 
                    concat([[x], *[acc]]), 
                 xs, ys)

def concat(lists):
    return foldl(lambda acc, xs: acc + xs, lists, [])

def filter(function, xs):
    return foldl(lambda acc, x: 
                    append(acc, [x]) if function(x) else acc,
                 xs, [])

def length(xs):
    return foldl(lambda acc, _: acc + 1, xs, 0)

def map(function, xs):
    return foldl(lambda acc, x: 
                    append(acc, [function(x)]), 
                 xs, [])

def foldl(function, xs, acc):
    if xs:
        head, *tail = xs
        xs = tail
        acc = foldl(function, tail, function(acc, head))
    return acc

def foldr(function, xs, acc):
    if xs:
        head, *tail = xs
        xs = tail
        acc = function(head, foldr(function, tail, acc))
    return acc

def reverse(xs):
    return foldr(lambda x, acc: 
                    append(acc, [x]), 
                 xs, [])