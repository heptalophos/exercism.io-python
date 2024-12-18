def find_anagrams(word, candidates):
    """
    detect which candidates 
    are anagrams of word
    """
    normalized = lambda x: sorted(x.lower())
    return [cand for cand in candidates 
                 if normalized(cand) == normalized(word)
                    and cand.lower() != word.lower()]
