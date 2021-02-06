def transform(legacy_data):
    shiny_new = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            shiny_new[letter.lower()] = score
    return shiny_new