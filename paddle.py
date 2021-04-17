from turtle import Turtle

class Paddle:

    _PADDLE_SEGMENT_HEIGHT_AND_WIDTH = 20
    _PADDLE_HEIGHT = 100

    def __init__(self, x_coordinate, y_coordinate):
        self.segments = []
        paddle = Turtle()
        paddle.shape('square')
        paddle.color('white')
        paddle.penup()
        paddle.setposition(x_coordinate, y_coordinate)
        paddle.setheading(90)
        paddle.turtlesize(1, 5)
        
