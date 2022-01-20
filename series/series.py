def slices(series, length):
    if series == "":
        raise ValueError("series cannot be empty")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length < 1:
        raise ValueError("slice length cannot be zero")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    return [series[n : n + length] for n in range(len(series) + 1 - length)]
    