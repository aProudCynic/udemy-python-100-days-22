from paddle import Paddle
from turtle import Screen
from constants import ARENA_WIDTH, ARENA_HEIGHT

def setup_gameplay_area(screen):
    screen.bgcolor('black')
    screen.setup(ARENA_WIDTH, ARENA_HEIGHT)
    screen.title('Pong')

screen = Screen()
setup_gameplay_area(screen)
screen.tracer(0)
paddle = Paddle(350, 0)
screen.update()
screen.exitonclick()
