from turtle import Turtle

class Paddle(Turtle):

    _PADDLE_MOVEMENT_DISTANCE = 10
    _PADDLE_HEIGHT = 100

    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.setposition(x_coordinate, y_coordinate)
        self.setheading(90)
        self.turtlesize(1, 5)
        
    def up(self):
        self.forward(Paddle._PADDLE_MOVEMENT_DISTANCE)

    def down(self):
        self.backward(Paddle._PADDLE_MOVEMENT_DISTANCE)
