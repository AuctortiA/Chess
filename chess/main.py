from chess_controller.window import Window
from chess_model.model import Model
from chess_view.canvas import Canvas

model = Model()
canvas = Canvas()
window = Window(model=model, canvas=canvas)

window.mainloop()
