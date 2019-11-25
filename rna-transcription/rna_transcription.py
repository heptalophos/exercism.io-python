import re

dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

def matches(s):
    return re.match("^([ACGT]+)+$", s)

def isDna(seq):
    return True if matches(seq) else False

def to_rna(dnaseq):
    rna = (dict[nucl] for nucl in dnaseq)
    return ''.join(rna) if isDna(dnaseq) else ""