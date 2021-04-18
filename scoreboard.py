from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.setposition(0, 270)
        self.score_left = 0
        self.score_right = 0
        self._write_score()

    def add_score_to_left(self):
        self.score_left += 1
        self._write_score()

    def add_score_to_right(self):
        self.score_right += 1
        self._write_score()

    def _write_score(self):
        self.clear()
        self.write(f'{self.score_left}:{self.score_right}', align='center', font=('Arial', 24))
