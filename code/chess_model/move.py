class Move:
    def __init__(self, old, new, board) -> None:

        self.old_rank, self.old_file = old
        self.new_rank, self.new_file = new

        self.old_piece = board[self.old_rank][self.old_file]
        self.new_piece = board[self.new_rank][self.new_file]

        if self.old_piece:
            self.old_piece_colour = self.old_piece.get_colour()
        else:
            self.old_piece_colour = None

        if self.new_piece:
            self.new_piece_colour = self.new_piece.get_colour()
        else:
            self.new_piece_colour = None

        self.rank_dif = self.new_rank - self.old_rank
        self.file_dif = self.new_file - self.old_file