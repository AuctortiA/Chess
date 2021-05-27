class Piece:
    def __init__(self, colour, square) -> None:
        self.colour = colour
        self.sqaure = square

class King (Piece):
    def __init__(self) -> None:
        super().__init__()

class Queen (Piece):
    def __init__(self) -> None:
        super().__init__()

class Rook (Piece):
    def __init__(self) -> None:
        super().__init__()

class Bishop (Piece): 
    def __init__(self) -> None:
        super().__init__()

class Knight(Piece):
    def __init__(self) -> None:
        super().__init__()

class Pawn (Piece):
    def __init__(self) -> None:
        super().__init__()

