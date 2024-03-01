SPIDER = "wriggled and jiggled and tickled inside her."
EDIBLES = ['fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse']
PERPLEXITIES = ['It wriggled and jiggled and tickled inside her.'
                'How absurd to swallow a bird!',
                'Imagine that, to swallow a cat!',
                'What a hog, to swallow a dog!',
                'Just opened her throat and swallowed a goat!',
                "I don't know how she swallowed a cow!"]
PREMISE = 'She swallowed the '
CONCLUSION = ' to catch the '
PROLOGUE = 'I know an old lady who swallowed a '
EPILOGUE = ["I don't know why she swallowed the fly. Perhaps she'll die.", 
            "She's dead, of course!"]

def recite(start_verse, end_verse):
    rhymes = []
    for v in range(start_verse, end_verse + 1):
        if rhymes: rhymes.append("")
        rhymes.append(PROLOGUE + EDIBLES[v - 1] + '.')
        if 2 <= v <= 7:
            rhymes.append(PERPLEXITIES[v - 2])
            for i in range(v - 1, 0, -1):
                if i == 2:
                    rhyme = PREMISE + EDIBLES[2] + CONCLUSION + \
                            EDIBLES[1] + ' that ' + SPIDER
                    rhymes.append(rhyme)
                    continue
                rhymes.append(PREMISE + EDIBLES[i] + \
                              CONCLUSION + EDIBLES[i - 1] + '.')
        if v <= 7:
            rhymes.append(EPILOGUE[0])
        else:
            rhymes.append(EPILOGUE[1])
    return rhymes


# def valid_verse_num (verse):
#     verse >= 1 and verse <= 8

# def first_line(verse):
#     line = ''
#     if verse >= 1 and verse < 8:
#         line += PROLOGUE + " " + EDIBLES[verse - 1] + '.'
#         if verse == 2: 
#             line += 'It ' + SPIDER + '.'
#     if verse == 8:
#         line = ''
#     return line

# def second_line(verse):
#     line = ''
#     if verse <= 2 or verse >= 8:
#         return line
#     if valid_verse_num:
#         line += PERPLEXITIES[verse - 3]
#     return line

# def stem_lines(verse):
#     lines = []
#     if verse <= 1 or verse >= 8:
#         return lines
#     while verse >= 2:
#         lines.append(PREMISE + EDIBLES[verse] + CONCLUSION + EDIBLES[verse - 1])
#         if verse == 2:
#             lines.append(' that ' + SPIDER)
#         verse -= 1
#     return lines

# def closing_line(verse):
#     epilogue = ''
#     if verse >= 1 and verse <= 7:
#         epilogue = EPILOGUE[0]
#     if verse == 8:
#         epilogue = EPILOGUE[1]
#     return epilogue

# def verse(n):
#     single_verse = []
#     single_verse.append(first_line(n))
#     single_verse.append(second_line(n))
#     single_verse.extend(stem_lines(n))
#     single_verse.append(closing_line(n))
#     return single_verse