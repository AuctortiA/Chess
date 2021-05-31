class Move:
    def __init__(self, old, new, board) -> None:

        self.old_rank, self.old_file = old
        self.new_rank, self.new_file = new

        self.old_piece = board[self.old_rank][self.old_file]
        self.new_piece = board[self.new_rank][self.new_file]

        self.old_piece_colour = self.__get_old_colour()
        self.new_piece_colour = self.__get_new_colour()

        self.rank_dif = self.new_rank - self.old_rank
        self.file_dif = self.new_file - self.old_file

    def __get_old_colour(self):
        if self.old_piece:
            return self.old_piece.get_colour()

    def __get_new_colour(self):
        if self.new_piece:
            return self.new_piece.get_colour()