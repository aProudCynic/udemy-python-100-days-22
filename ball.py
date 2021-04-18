from turtle import Turtle


class Ball(Turtle):

    HEIGHT_AND_WIDTH = 20

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setheading(50)

    def bounce_horizontally(self):
        self.setheading(self.heading() * -1)