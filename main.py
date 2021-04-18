from time import sleep
from paddle import Paddle
from turtle import Screen
from constants import ARENA_WIDTH, ARENA_HEIGHT

def setup_event_listeners(screen, paddle: Paddle):
    screen.listen()
    screen.onkey(paddle.up, 'Up')
    screen.onkey(paddle.down, 'Down')

def setup_gameplay_area(screen):
    screen.bgcolor('black')
    screen.setup(ARENA_WIDTH, ARENA_HEIGHT)
    screen.title('Pong')
    screen.tracer(0)

screen = Screen()
setup_gameplay_area(screen)
paddle = Paddle(350, 0)
setup_event_listeners(screen, paddle)
screen.update()

game_on = True
while game_on:
    screen.update()

screen.exitonclick()
