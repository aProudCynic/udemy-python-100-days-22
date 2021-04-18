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

def ball_hits_paddle(ball, left_paddle, right_paddle):
    ball_x_coordinate = ball.xcor()
    offset_for_ball_and_paddle_width = (Ball.HEIGHT_AND_WIDTH + Paddle.WIDTH) / 2
    ball_in_line_with_left_paddle = ball_x_coordinate <= left_paddle.xcor() + offset_for_ball_and_paddle_width
    ball_in_line_with_rigth_paddle = ball_x_coordinate >= right_paddle.xcor() - offset_for_ball_and_paddle_width
    if ball_in_line_with_left_paddle:
        return ball_touches_paddle(ball, left_paddle)
    elif ball_in_line_with_rigth_paddle:
        return ball_touches_paddle(ball, right_paddle)

def ball_touches_paddle(ball: Ball, paddle: Paddle):
    paddle_y_coordinate = paddle.ycor()
    ball_y_coordinate = ball.ycor()
    return ball_y_coordinate <= paddle_y_coordinate + Paddle.HEIGHT and ball_y_coordinate >= paddle_y_coordinate - Paddle.HEIGHT

def ball_hits_vertical_wall(ball: Ball):
    return ball_hits_left_wall(ball) or ball_hits_right_wall(ball)

def ball_hits_left_wall(ball: Ball):
    ball_x_coordinate = ball.xcor()
    ball_coordinate_to_touch_left_wall = (ARENA_WIDTH / 2 - Ball.HEIGHT_AND_WIDTH) * -1
    return ball_x_coordinate <= ball_coordinate_to_touch_left_wall

def ball_hits_right_wall(ball: Ball):
    ball_x_coordinate = ball.xcor()
    ball_coordinate_to_touch_right_wall = ARENA_WIDTH / 2 - Ball.HEIGHT_AND_WIDTH
    return ball_x_coordinate >= ball_coordinate_to_touch_right_wall

def evaluate_winner(ball: Ball):
    if ball_hits_left_wall(ball):
        return ('right player won')
    elif ball_hits_right_wall(ball):
        return ('left player won')

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
    if ball_hits_paddle(ball, left_paddle, right_paddle):
        ball.bounce_vertically()
    if ball_hits_vertical_wall(ball):
        game_on = False
        print(evaluate_winner(ball))
    else:
        ball.forward(5)
        screen.update()

screen.exitonclick()
