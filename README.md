# Chess Project

## Design
I chose to use the model-view-controller design pattern for my chess application. This consists of 3 main parts: the model - manipulating and storing the state of the board and pieces; the view - representing the state of the board and pieces in a GUI; and finally the controller - requesting changes to the model based on user input. 

This design pattern allows my solution to be far more readable and maintainable through abstraction, as the model and view are loosely coupled by an optional delegate class. It also improves cross compatibility with different libraries or even languages for the logic or graphical part of my solution.
