class Queen:
    def __init__(self, rank, file):
        negative = "row" if rank < 0 else "column" if file < 0 else "ok"
        if negative != "ok":
            raise ValueError(f'{negative} not positive')
        outsider = "row" if rank > 7 else "column" if file > 7 else "ok"
        if outsider !="ok":
            raise ValueError(f'{outsider} not on board')
        self.rank, self.file = rank, file

    def can_attack(self, another_queen):
        err = 'Invalid queen position: both queens in the same square'
        drank = abs(self.rank - another_queen.rank)
        dfile = abs(self.file - another_queen.file)
        if drank == dfile == 0:
            raise ValueError(err)
        return drank * dfile == 0 or drank / dfile == 1
