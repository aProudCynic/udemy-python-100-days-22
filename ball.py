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
        new_heading = self.heading() * -1
        self.setheading(new_heading)

    def bounce_vertically(self):
        new_heading = 180 - self.heading()
        self.setheading(new_heading)