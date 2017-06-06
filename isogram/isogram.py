def is_isogram(input):
    normal = [char.lower() for char in input if char.isalpha()]
    return len(set(normal)) == len(normal)

