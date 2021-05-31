import pygame as pg
import os


class Canvas:
    def __init__(self, scale) -> None:
        # pygame
        self.scale = scale

        # board
        self.ranks = 8
        self.files = 8

        self.square_rects = [[] for _ in range(self.ranks)]

        for rank in range(self.ranks):
            for file in range(self.files):
                self.square_rects[rank].append(pg.Rect(file * self.scale, rank * self.scale, self.scale, self.scale))

        # pieces 
        self.piece_imgs = {}
        piece_set = "cburnett"
        piece_path = os.path.join("resources", "pieces", piece_set)

        #   import black piece images
        black_piece_path = os.path.join(piece_path, "black")
        for img in os.listdir(black_piece_path):
            add_pg_img (self.piece_imgs, img, black_piece_path, self.scale)

        #   import white piece images
        white_piece_path = os.path.join(piece_path, "white")
        for img in os.listdir(white_piece_path):
            add_pg_img (self.piece_imgs, img, white_piece_path, self.scale)
        
        self.piece_names = self.piece_imgs.keys()

        
    def render(self, win, fen, dragged_piece=None, dragged_pos=None, w_controlled_squares=[]):
        
        # board
        self.render_board(win, w_controlled_squares)

        # pieces
        self.render_pieces(win, fen, dragged_piece, dragged_pos)

    def render_board(self, win, w_controlled_squares): 
        
        LIGHT_SQUARE = (240,217,181)
        DARK_SQUARE = (181,136,99)

        for rank in range(self.ranks):
            for file in range(self.files):
                colour = LIGHT_SQUARE if (rank + file) % 2 == 0 else DARK_SQUARE

                if (rank, file) in w_controlled_squares:
                    colour = (100, 0, 0)

                pg.draw.rect(win, colour, self.square_rects[rank][file])

    def render_pieces(self, win, fen, dragged_piece, dragged_pos):
        
        rank_num = 0
        file_num = 0

        if dragged_piece:
            d_rank, d_file = dragged_piece

        dragged_char = None

        for char in fen:
            if char in self.piece_names:

                if dragged_piece:
                    if d_rank == rank_num and d_file == file_num:
                        dragged_char = char
                    else:
                        self.render_piece(win, rank_num, file_num, char)

                else:
                    self.render_piece(win, rank_num, file_num, char)

                file_num += 1

            elif char.isdigit():
                file_num += int(char)
            
            elif char == "/":
                rank_num += 1
                file_num = 0
            
            else:
                break
            
        if dragged_char:
            self.render_piece (win, d_rank, file_num, dragged_char, dragged_pos)

    def render_piece(self, win, rank, file, piece, dragged_pos=None):
        if dragged_pos:
            drag_rect = pg.Rect(dragged_pos, (self.scale, self.scale))
            drag_rect.center = dragged_pos
            win.blit(self.piece_imgs[piece], drag_rect)
        else:
            win.blit(self.piece_imgs[piece], self.square_rects[rank][file])


def add_pg_img (_dict, img_name, path, scale):
    _dict.update(
                {img_name[0]:   pg.transform.smoothscale(
                                pg.image.load(os.path.join(path, img_name)),
                                ((scale), (scale)))
                }
            )