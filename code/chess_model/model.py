from chess_model.pieces import King, Queen, Rook, Bishop, Knight, Pawn


class Model:
    def __init__(self, fen) -> None:


        self.ranks = 8
        self.files = 8

        # game state
        self.turn = "w"
        self.board = [[None for _ in range(self.files)] for _ in range (self.ranks)]

        self.fen_piece_codes = {"k": King, "q": Queen, "r": Rook, "b": Bishop, "n": Knight, "p": Pawn}

        file_num = 0
        rank_num = 0

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

    def move(self, old, new) -> None:
        old_rank, old_file = old
        piece = self.board[old_rank][old_file]
        if piece:
            if piece.valid_move(old, new):
                if self.valid_move(old, new):
                    self.board [old_rank][old_file] = None

                    new_rank, new_file = new
                    self.board [new_rank][new_file] = piece

                    self.turn = "b" if self.turn == "w" else "w"

    def valid_move(self, old, new) -> bool:
        return  self.check_turn(old, new) and \
                self.check_friendly_capture(old, new) 
                
    def check_turn (self, old, new):
        old_rank, old_file = old
        old_piece_colour = self.board[old_rank][old_file].get_colour()

        return old_piece_colour == self.turn

    def check_friendly_capture(self, old, new) -> bool:
        
        new_rank, new_file = new
        new_piece = self.board[new_rank][new_file]
        if not new_piece:
            return True

        new_piece_colour = new_piece.get_colour()

        old_rank, old_file = old
        old_piece_colour = self.board[old_rank][old_file].get_colour()
    
        return old_piece_colour != new_piece_colour