def transform(legacy_data):
    new_data = {}
    for k, v in legacy_data.items():
        for item in v:
            new_data[item.lower()] = k
    return new_data