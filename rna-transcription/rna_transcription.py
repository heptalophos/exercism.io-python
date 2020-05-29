import re

RNA_TRANSCRIPTION = {'G': 'C', 
                     'C': 'G', 
                     'T': 'A', 
                     'A': 'U'}

def isDna(seq):
    if re.match("^[ACGT]+$", seq):
        return True
    else: 
        return False

def to_rna(dnaseq):
    if isDna(dnaseq):
        return ''.join(RNA_TRANSCRIPTION[nucl] 
                       for nucl in dnaseq) 
    else: 
        return ""