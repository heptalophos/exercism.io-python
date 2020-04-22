def flatten(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten(item))
        elif item is not None:
            flat.append(item) 
        else:
            pass
    return flat