from chess_model.pieces import King, Queen, Rook, Bishop, Knight, Pawn
from chess_model.move import Move


class Model:
    def __init__(self, fen) -> None:
        
        self.fen_piece_codes = {"k": King, "q": Queen, "r": Rook, "b": Bishop, "n": Knight, "p": Pawn}
        
        self.ranks = 8
        self.files = 8

        # game state
        self.turn = "w"
        self.board = self.populate_board()
        self.valid_moves = self.get_valid_moves()

    def __str__ (self) -> str:

        fen = ""
        empty_num = 0

        for rank in self.board:
            for square in rank:
                if square:
                    if empty_num != 0:
                        fen += str(empty_num)
                        empty_num = 0

                    fen += str(square)
                else:
                    empty_num += 1

            if empty_num != 0:
                fen += str(empty_num)
            
            fen += "/"
            empty_num = 0

        return fen

    def populate_board (self, fen):
        #   populate board
        file_num = 0
        rank_num = 0

        board = [[None for _ in range(self.files)] for _ in range (self.ranks)]
        for char in fen:
            piece_class = self.fen_piece_codes.get(char.lower())

            if piece_class:
                piece = piece_class(char, file_num, rank_num)
                self.board[rank_num][file_num] = piece
                file_num += 1

            elif char.isdigit():
                file_num += int(char)
            
            elif char == "/":
                rank_num += 1
                file_num = 0
            else:
                break

        return board

    def move(self, old, new) -> None:
        
        _move = Move(old, new, self.board)

        if _move.old_piece:
            if _move.old_piece.valid_move(_move):
                if self.valid_move(_move):
                    
                    # update board
                    self.board [_move.old_rank][_move.old_file] = None
                    new_rank, new_file = new
                    self.board [new_rank][new_file] = _move.old_piece

                    # update piece
                    _move.old_piece.rank, _move.old_piece.piece = new

                    # update game state
                    self.turn = "b" if self.turn == "w" else "w"

    def update_valid_moves (self):
        



    def valid_move(self, _move) -> bool:

        if type(_move.old_piece) is King:
            self.check_moving_into_check

        if type(_move.old_piece) is Pawn:
            if not self.check_pawn_capture(_move):
                return False
            
            if not self.check_pawn_two_square_rule(_move):
                return False

            if not self.check_pawn_forward_move(_move):
                return False

        return  self.check_turn(_move) and \
                self.check_friendly_capture(_move) and \
                self.check_blocking_pieces(_move) and \
                self.check_in_check(_move) 
                
    def check_turn (self, _move):
        return _move.old_piece_colour == self.turn

    def check_friendly_capture(self, _move) -> bool:
        if not _move.new_piece:
            return True
        return _move.old_piece_colour != _move.new_piece_colour

    def check_blocking_pieces(self, _move) -> bool:
        if not type(_move.old_piece) is Knight:
            
            # diagonal
            if abs(_move.rank_dif) == abs(_move.file_dif):
                if _move.rank_dif < 0:
                    if _move.file_dif > 0:
                        # north-east
                        for square_dif in range(1, abs(_move.rank_dif)):
                            if self.board[_move.old_rank - square_dif][_move.old_file + square_dif]:
                                return False
                    else:
                        # north-west
                        for square_dif in range(1, abs(_move.rank_dif)):
                            if self.board[_move.old_rank - square_dif][_move.old_file - square_dif]:
                                return False
                else:
                    if _move.file_dif > 0:
                        # south-east
                        for square_dif in range(1, abs(_move.rank_dif)):
                            if self.board[_move.old_rank + square_dif][_move.old_file + square_dif]:
                                return False
                    else:
                        # south-west
                        for square_dif in range(1, abs(_move.rank_dif)):
                            if self.board[_move.old_rank + square_dif][_move.old_file - square_dif]:
                                return False
                    
            # vertical & horizontal
            if (_move.rank_dif != 0 and _move.file_dif == 0) or (_move.rank_dif == 0 and _move.file_dif != 0):
                if _move.rank_dif < 0:
                    # north
                    for square_dif in range(1, abs(_move.rank_dif)):
                        if self.board[_move.old_rank - square_dif][_move.old_file]:
                            return False

                elif _move.rank_dif > 0:
                    # south
                    for square_dif in range(1, abs(_move.rank_dif)):
                        if self.board[_move.old_rank + square_dif][_move.old_file]:
                            return False

                elif _move.file_dif > 0:
                    # east
                    for square_dif in range(1, abs(_move.file_dif)):
                        if self.board[_move.old_rank][_move.old_file + square_dif]:
                            return False

                else:
                    # west
                    for square_dif in range(1, abs(_move.file_dif)):
                        if self.board[_move.old_rank][_move.old_file - square_dif]:
                            return False
        return True

    def check_pawn_capture(self, _move) -> bool:
        if abs(_move.rank_dif) == 1 and abs(_move.file_dif) == 1:
            return self.board[_move.new_rank][_move.new_file]
        return True
    
    def check_pawn_two_square_rule(self, _move) -> bool:
        if abs(_move.rank_dif) == 2:
            if _move.old_rank == 1 or _move.old_rank == self.ranks - 2:
                return True
            else:
                return False

        return True

    def check_pawn_forward_move(self, _move) -> bool:
        
        if 0 <= abs(_move.rank_dif) <= 2 and _move.file_dif == 0:
            if _move.new_piece:
                return False
        return True

    def check_in_check(self, _move) -> bool:
        # get kings
        for rank in self.board:
            for piece in rank:
                if type(piece) is King:
                    

    
    def check_moving_into_check(self, _move) -> bool:
        return True