def reverse(string):
    if len(string) == 1 or len(string) == 0:
        return string
    else:
        return "{}{}{}".format(string[-1], 
                               reverse(string[1:-1]), 
                               string[0])