class Piece:
    def __init__(self, code, file, rank) -> None:
        self.code = code

        self.file = file
        self.rank = rank

    def __str__(self):
        return self.code

    def valid_move(self, old, new):
        return True


class King (Piece):
    def __init__(self, code, file, rank) -> None:
        super().__init__(code, file, rank)

    def valid_move(self, old, new):
        old_rank, old_file = old
        new_rank, new_file = new

        rank_dif = old_rank - new_rank
        file_dif = old_file - new_file 

        return -1 <= rank_dif <= 1 and -1 <= file_dif <= 1
        

class Queen (Piece):
    def __init__(self, code, file, rank) -> None:
        super().__init__(code, file, rank)

    def valid_move(self, old, new):
        old_rank, old_file = old
        new_rank, new_file = new

        rank_dif = old_rank - new_rank
        file_dif = old_file - new_file 


class Rook (Piece):
    def __init__(self, code, file, rank) -> None:
        super().__init__(code, file, rank)

    def valid_move(self, old, new):
        old_rank, old_file = old
        new_rank, new_file = new

        rank_dif = old_rank - new_rank
        file_dif = old_file - new_file 


class Bishop (Piece): 
    def __init__(self, code, file, rank) -> None:
        super().__init__(code, file, rank)

    def valid_move(self, old, new):
        old_rank, old_file = old
        new_rank, new_file = new

        rank_dif = old_rank - new_rank
        file_dif = old_file - new_file  


class Knight (Piece):
    def __init__(self, code, file, rank) -> None:
        super().__init__(code, file, rank)

    def valid_move(self, old, new):
        old_rank, old_file = old
        new_rank, new_file = new

        rank_dif = old_rank - new_rank
        file_dif = old_file - new_file 

class Pawn (Piece):
    def __init__(self, code, file, rank) -> None:
        super().__init__(code, file, rank)

    def valid_move(self, old, new):
        old_rank, old_file = old
        new_rank, new_file = new

        rank_dif = old_rank - new_rank
        file_dif = old_file - new_file 

        if 0 <= rank_dif <= 2 and file_dif == 0:
            return True
        
        if rank_dif == 1 and -1 <= file_dif <= 1:
            return True

        return False
