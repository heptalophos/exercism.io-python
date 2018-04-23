def slices(series, length):
    digits = [int(d) for d in series]
    if len(digits) < length or length < 1:
        raise ValueError("Length not appropriate")
    return [digits[n : n + length] for n in range(len(digits) + 1 - length)]
