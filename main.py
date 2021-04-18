from time import sleep
from paddle import Paddle
from turtle import Screen
from constants import ARENA_WIDTH, ARENA_HEIGHT

def setup_event_listeners(paddle: Paddle, up_key: str, down_key: str):
    screen.onkey(paddle.up, up_key)
    screen.onkey(paddle.down, down_key)

def setup_gameplay_area(screen):
    screen.bgcolor('black')
    screen.setup(ARENA_WIDTH, ARENA_HEIGHT)
    screen.title('Pong')
    screen.tracer(0)

screen = Screen()
setup_gameplay_area(screen)
left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
screen.listen()
setup_event_listeners(left_paddle, 'w', 's')
setup_event_listeners(right_paddle, 'Up', 'Down')
screen.update()

game_on = True
while game_on:
    screen.update()

screen.exitonclick()
