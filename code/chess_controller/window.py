import pygame as pg

import math


class Window: 
    def __init__(self, model, canvas, scale) -> None:
        
        # modules
        self.model = model
        self.canvas = canvas
        
        # game state
        self.fen = str(model) # get fen
        
        # window state
        self.changes = True

        self.scale = scale
        self.piece_dragged = False

        # init pygame
        pg.init()

        self.quit = False

        # pygame objects
        self.win = pg.display.set_mode((8 * scale, 8 * scale))
        pg.display.set_caption("Chess")
        
        self.clock = pg.time.Clock()

    def handle_events(self):

        # event loop all in one function to reduce no. times looping through events
        for event in self.events:

            # handle quit
            if event.type == pg.QUIT:
                self.quit = True

            elif event.type == pg.MOUSEBUTTONDOWN:
                self.changes = True

                # get corresponding file/rank
                if not self.piece_dragged:
                    x, y = pg.mouse.get_pos()

                    rank = math.floor(y / self.scale)
                    file = math.floor(x / self.scale)

                    self.piece_dragged = (rank, file)

            elif event.type == pg.MOUSEBUTTONUP:
                self.changes = True
                if self.piece_dragged:
                    x, y = pg.mouse.get_pos()

                    new_rank = math.floor(y / self.scale)
                    new_file = math.floor(x / self.scale)

                    self.model.move(self.piece_dragged, (new_rank, new_file))
                    self.piece_dragged = False

        
    def loop(self):
        
        # events
        self.events = pg.event.get()
        self.handle_events()

        # render
        if self.changes or self.piece_dragged:
            self.fen = str(self.model)

            if self.piece_dragged:
                pos = pg.mouse.get_pos()
                self.canvas.render(self.win, self.fen, self.piece_dragged, pos)
            else:
                self.canvas.render(self.win, self.fen)
        
        self.changes = False


        # pygame objects
        self.clock.tick(165)
        pg.display.update()