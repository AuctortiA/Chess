from chess_controller.window import Window
from chess_model.model import Model
from chess_view.canvas import Canvas

scale = 150
fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

model = Model(fen)
canvas = Canvas(scale)

window = Window(model, canvas, scale)


# mainloop
while not window.quit:
    window.loop()
