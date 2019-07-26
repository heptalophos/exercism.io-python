from itertools import takewhile

CMap = (
    (('AUG',),'Methionine'),
    (('UUU', 'UUC'),'Phenylalanine'),
    (('UUA', 'UUG'),'Leucine'),
    (('UCU', 'UCC', 'UCA', 'UCG'),'Serine'),
    (('UAU', 'UAC'),'Tyrosine'),
    (('UGU', 'UGC'),'Cysteine'),
    (('UGG',),'Tryptophan'),
    (('UAA', 'UAG', 'UGA'),'STOP'))

codons = { codon: amino for codons, amino in CMap for codon in codons }

def proteins(strand):
    pchain = ["".join(c) for c in zip(*([iter(strand)] * 3))]
    return [aminoacid for aminoacid in list(takewhile(lambda codon: codon != 'STOP', 
                                                      [a for a in (codons[c] 
                                                                   for c in pchain)]))]
