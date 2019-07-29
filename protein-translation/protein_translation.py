from itertools import takewhile

CMap = (
    (('AUG',), 'Methionine'),
    (('UUU', 'UUC'), 'Phenylalanine'),
    (('UUA', 'UUG'), 'Leucine'),
    (('UCU', 'UCC', 'UCA', 'UCG'), 'Serine'),
    (('UAU', 'UAC'), 'Tyrosine'),
    (('UGU', 'UGC'), 'Cysteine'),
    (('UGG',), 'Tryptophan'),
    (('UAA', 'UAG', 'UGA'), 'STOP'))

codons = {codon: amino for cods, amino in CMap
          for codon in cods}


def proteins(strand):
    return [aminoacid for aminoacid in list(
        takewhile(lambda codon: codon != 'STOP',
                  [aa for aa in (codons[cd]
                                 for cd in ["".join(nuc)
                                            for nuc in
                                            zip(*([iter(strand)] * 3))])]))]
