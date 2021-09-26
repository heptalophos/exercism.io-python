def reverse(string):
    return (len(string) > 1 and reverse(string[1:]) + string[0]) or string
