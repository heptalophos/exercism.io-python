import re

TRANSCRIPTION = {
    'G': 'C', 
    'C': 'G', 
    'T': 'A', 
    'A': 'U'
}

def isDna(seq):
    if re.match("^[ACGT]+$", seq):
        return True
    return False

def to_rna(dnaseq):
    if isDna(dnaseq):
        return ''.join(TRANSCRIPTION[nucl] 
                       for nucl in dnaseq) 
    return ""