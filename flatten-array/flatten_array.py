def flatten(anylist):
    flat = []
    for item in anylist:
        if isinstance(item, list):
            flat.extend(flatten(item))
        elif item is not None:
            flat.append(item) 
        else:
            pass
    return flat