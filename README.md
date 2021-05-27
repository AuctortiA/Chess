# Chess Project

## Design
I chose to use the model-delegate design pattern for my chess application. This consists of 3 main parts: the model - storing the state of the board and pieces; the view - representing the state of the board and pieces in a GUI and handling user input through this GUI; and finally the delegate - loosely linking the user input from the view to methods in the model, that in turn cause events that the delegate can then pass onto the view. 

This design pattern allows my solution to be far more readable and maintainable through abstraction, as the model and view are loosely coupled by an optional delegate class. It also improves cross compatibility with different libraries or even languages for the logic or graphical part of my solution.
