from time import sleep
from paddle import Paddle
from turtle import Screen
from constants import ARENA_WIDTH, ARENA_HEIGHT

def setup_gameplay_area(screen):
    screen.bgcolor('black')
    screen.setup(ARENA_WIDTH, ARENA_HEIGHT)
    screen.title('Pong')
    screen.tracer(0)

screen = Screen()
setup_gameplay_area(screen)
paddle = Paddle(350, 0)
screen.update()

game_on = True
while game_on:
    screen.update()
    sleep(0.2)

screen.exitonclick()
