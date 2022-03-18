from itertools import takewhile

CodonMap = (
    (('AUG',), 'Methionine'),
    (('UUU', 'UUC'), 'Phenylalanine'),
    (('UUA', 'UUG'), 'Leucine'),
    (('UCU', 'UCC', 'UCA', 'UCG'), 'Serine'),
    (('UAU', 'UAC'), 'Tyrosine'),
    (('UGU', 'UGC'), 'Cysteine'),
    (('UGG',), 'Tryptophan'),
    (('UAA', 'UAG', 'UGA'), 'STOP'))

codons = {codon: aminoacid for codons, 
                 aminoacid in CodonMap 
                 for codon in codons}

def proteins(strand):
    aminoacids = [a for a in (codons[c]
                    for c in ["".join(nuc) 
                              for nuc in zip(*([iter(strand)] * 3))])]
    return [aminoacid 
            for aminoacid in list(
                takewhile(
                    lambda codon: codon != 'STOP', aminoacids)
                )]
