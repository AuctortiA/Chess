def check_in_check(self, _model):
    # could store this separtely but operation isn't too expensive i don't think (worth verifying?)

        unpinned_piece = False

        for rank in self.board:
            for piece in rank:
                if type(piece) is King and piece.get_colour() == _move.old_piece_colour:

                    # diagonal
                    rank_check = piece.rank
                    file_check = piece.file

                    while True:
                        rank_check += 1
                        file_check += 1

                        if not (0 <= rank_check < self.ranks and 0 <= file_check < self.files):
                            break
                        
                        piece = self.board[rank_check][file_check]

                        if piece:
                            if type(piece) in [Queen, Bishop]:
                                return False
                            else:
                                if rank_check == _move.old_rank and file_check == _move.old_file:
                                    unpinned_piece = True
                                else: 
                                    break
                        
                        # checking this is quicker than checking every visible square after the move is made.
                        if rank_check == _move.new_rank and file_check == _move.new_file:
                            unpinned_piece = False
        
        return not unpinned_piece