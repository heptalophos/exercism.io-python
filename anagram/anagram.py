def detect_anagrams(word, candidates):
    """
    detect which candidates members are anagrams of word
    """
    return [candidate for candidate in candidates if sorted(candidate.lower()) == sorted(word.lower())
                                                     and candidate.lower() != word.lower()
           ]
