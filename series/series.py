def slices(series, length):
    if len(series) < length or length < 1:
        raise ValueError("slice length cannot be greater than series length")
    return [series[n : n + length] for n in range(len(series) + 1 - length)]
    