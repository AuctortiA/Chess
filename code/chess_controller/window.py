import pygame as pg

class Window: 
    def __init__(self, model, canvas) -> None:
        
        # modules
        self.model = model
        self.canvas = canvas

        # init pygame
        pg.init()

        self.quit = False

        # pygame objects
        self.win = pg.display.set_mode((800, 800))
        pg.display.set_caption("Chess")
        
        self.clock = pg.time.Clock()

    def handle_events(self):
        # event loop

        for event in self.events:
            if event.type == pg.QUIT:
                self.quit = True


    def loop(self):

        # render
        self.canvas.render(self.win)
        
        # events
        self.events = pg.event.get()
        self.handle_events()

        # pygame objects
        self.clock.tick(60)
        pg.display.update()