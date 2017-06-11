import re

dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

def isDna(seq):
    return True if re.match("^([ACGT]+)+$", seq) else False

def to_rna(dnaseq):
    return ''.join(dict[nucl] for nucl in dnaseq) if isDna(dnaseq) else ""
