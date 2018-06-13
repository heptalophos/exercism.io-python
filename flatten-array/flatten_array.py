def flatten(iterable):
    flat = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            flat += flatten(item)
        elif item is not None:
            flat.append(item) 
        else:
            pass
    return flat