def is_isogram(input):
    sanitized = [char.lower() for char in input if char.isalpha()]
    return len(set(sanitized)) == len(sanitized)