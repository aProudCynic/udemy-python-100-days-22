from ball import Ball
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

def ball_hits_horizontal_wall(ball: Ball):
    max_up_coordinate = ARENA_HEIGHT / 2 - Ball.HEIGHT_AND_WIDTH
    max_down_coordinate = max_up_coordinate * -1
    ball_y_coordinate = ball.ycor()
    return ball_y_coordinate >= max_up_coordinate or ball_y_coordinate <= max_down_coordinate

screen = Screen()
setup_gameplay_area(screen)
left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
screen.listen()
setup_event_listeners(left_paddle, 'w', 's')
setup_event_listeners(right_paddle, 'Up', 'Down')
screen.update()

game_on = True
while game_on:
    if ball_hits_horizontal_wall(ball):
        ball.bounce_horizontally()
    ball.forward(5)
    screen.update()

screen.exitonclick()
