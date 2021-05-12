def slices(series, length):
    if len(series) < length or length < 1:
        raise ValueError("Length not appropriate")
    return [series[n : n + length] for n in 
            range(len(series) + 1 - length)]