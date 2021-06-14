class Piece:
    def __init__(self, code, file, rank) -> bool:
        self.code = code

        self.file = file
        self.rank = rank

    def __str__(self):
        return self.code
    
    def __iter__(self):
        yield self.file
        yield self.rank
        
    def valid_move(self, _move):
        return True

    def get_colour (self):
        return "w" if self.code.isupper() else "b"

class King (Piece):
    def __init__(self, code, file, rank) -> bool:
        super().__init__(code, file, rank)

    def valid_move(self, _move):
        return -1 <= _move.rank_dif <= 1 and -1 <= _move.file_dif <= 1
    

class Queen (Piece):
    def __init__(self, code, file, rank) -> bool:
        super().__init__(code, file, rank)

    def valid_move(self, _move):
        if _move.rank_dif != 0 and _move.file_dif == 0:
            return True
        
        if _move.rank_dif == 0 and _move.file_dif != 0:
            return True

        return abs(_move.rank_dif) == abs(_move.file_dif)


class Rook (Piece):
    def __init__(self, code, file, rank) -> bool:
        super().__init__(code, file, rank)

    def valid_move(self, _move):
        if _move.rank_dif != 0 and _move.file_dif == 0:
            return True
        
        if _move.rank_dif == 0 and _move.file_dif != 0:
            return True
        
        return False


class Bishop (Piece): 
    def __init__(self, code, file, rank) -> bool:
        super().__init__(code, file, rank)

    def valid_move(self, _move):
        return abs(_move.rank_dif) == abs(_move.file_dif)


class Knight (Piece):
    def __init__(self, code, file, rank) -> bool:
        super().__init__(code, file, rank)

    def valid_move(self, _move):
        if abs(_move.rank_dif) == 1 and abs(_move.file_dif) == 2:
            return True
        
        if abs(_move.rank_dif) == 2 and abs(_move.file_dif) == 1:
            return True

        return False


class Pawn (Piece):
    def __init__(self, code, file, rank) -> bool:
        super().__init__(code, file, rank)

    def valid_move(self, _move):
        if self.code.isupper():
            if -2 <= _move.rank_dif <= 0 and _move.file_dif == 0:
                return True
            
            if _move.rank_dif == -1 and -1 <= _move.file_dif <= 1:
                return True
        else:
            if 0 <= _move.rank_dif <= 2 and _move.file_dif == 0:
                return True
            
            if _move.rank_dif == 1 and -1 <= _move.file_dif <= 1:
                return True
        return False
