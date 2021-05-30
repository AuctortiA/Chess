class Piece:
    def __init__(self, code, file, rank) -> None:
        self.code = code

        self.file = file
        self.rank = rank

    def __str__(self):
        return self.code


class King (Piece):
    def __init__(self, code, file, rank) -> None:
        super().__init__(code, file, rank)


class Queen (Piece):
    def __init__(self, code, file, rank) -> None:
        super().__init__(code, file, rank)


class Rook (Piece):
    def __init__(self, code, file, rank) -> None:
        super().__init__(code, file, rank)


class Bishop (Piece): 
    def __init__(self, code, file, rank) -> None:
        super().__init__(code, file, rank)


class Knight (Piece):
    def __init__(self, code, file, rank) -> None:
        super().__init__(code, file, rank)


class Pawn (Piece):
    def __init__(self, code, file, rank) -> None:
        super().__init__(code, file, rank)

