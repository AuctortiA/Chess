from chess_model.pieces import King, Queen, Rook, Bishop, Knight, Pawn


class Model:
    def __init__(self, fen) -> None:

        self.ranks = 8
        self.files = 8

        self.board = [[[] for _ in range(self.files)] for _ in range (self.ranks)]

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

    def __str__ (self):
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

    def move(self, old, new):
        old_rank, old_file = old
        piece = self.board[old_rank][old_file]

        self.board [old_rank][old_file] = None

        new_rank, new_file = new
        self.board [new_rank][new_file] = piece