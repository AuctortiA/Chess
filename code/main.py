from chess_controller.window import Window
from chess_model.model import Model
from chess_view.canvas import Canvas

scale = 150
model = Model()
canvas = Canvas(scale)

window = Window(model, canvas, scale)


# mainloop
while not window.quit:
    window.loop()
