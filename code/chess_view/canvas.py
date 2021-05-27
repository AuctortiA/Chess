import pygame as pg
import os

class Canvas:
    def __init__(self, model) -> None:
        # pygame
        self.scale = 100

        self.model = model 

        # board
        self.ranks = 8
        self.files = 8

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
        
        
    def render(self, win):
        
        # board
        self.render_board(win)

        # pieces
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" # model.get_fen()
        self.render_pieces(win, fen)

    def render_board(self, win): 
        LIGHT_SQUARE = (240,217,181)
        DARK_SQUARE = (181,136,99)

        for file in range(self.files):
            for rank in range(self.ranks):
                colour = LIGHT_SQUARE if (rank + file) % 2 == 0 else DARK_SQUARE
                pg.draw.rect(win, colour, pg.Rect(file * self.scale, rank * self.scale, self.scale, self.scale))

    def render_pieces(self, win, fen):
        for piece in fen:
            pass


def add_pg_img (_dict, img_name, path, scale):
    _dict.update(
                {img_name[0]:   pg.transform.scale(
                                pg.image.load(os.path.join(path, img_name)),
                                ((22 * scale), (22 * scale)))
                }
            )