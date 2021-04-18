from ball import Ball
from paddle import Paddle
from turtle import Screen
from constants import ARENA_WIDTH, ARENA_HEIGHT
from scoreboard import Scoreboard

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
        print(f'ball_in_line_with_left_paddle at {ball_x_coordinate}')
        touch_paddle = ball_touches_paddle(ball, left_paddle)
        print(f'ball touches left_paddle: {touch_paddle}')
        return touch_paddle
    elif ball_in_line_with_rigth_paddle:
        print(f'ball_in_line_with_right_paddle {ball_x_coordinate}')
        touch_paddle = ball_touches_paddle(ball, right_paddle)
        print(f'ball touches right_paddle: {touch_paddle}')
        return touch_paddle

def ball_touches_paddle(ball: Ball, paddle: Paddle):
    paddle_y_coordinate = paddle.ycor()
    ball_y_coordinate = ball.ycor()
    ball_heading = ball.heading()
    ball_moves_towards_paddle = ball_heading < 90 or ball_heading > 270 if paddle.xcor() > 0 else ball_heading > 90 and ball_heading < 270
    return ball_moves_towards_paddle and ball_y_coordinate <= paddle_y_coordinate + Paddle.HEIGHT / 2 and ball_y_coordinate >= paddle_y_coordinate - Paddle.HEIGHT / 2

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

def evaluate_winner(ball: Ball, scoreboard: Scoreboard):
    if ball_hits_left_wall(ball):
        scoreboard.add_score_to_right()
        ball.setheading(-50)
    elif ball_hits_right_wall(ball):
        scoreboard.add_score_to_left()
        ball.setheading(50)
    ball.setpos(0, 0)

screen = Screen()
setup_gameplay_area(screen)
left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
setup_event_listeners(left_paddle, 'w', 's')
setup_event_listeners(right_paddle, 'Up', 'Down')
screen.update()

game_on = True
while game_on:
    if ball_hits_horizontal_wall(ball):
        ball.bounce_horizontally()
        print(f'new direction: {ball.heading()}')
    if ball_hits_paddle(ball, left_paddle, right_paddle):
        ball.bounce_vertically()
        print(f'new direction: {ball.heading()}')
    if ball_hits_vertical_wall(ball):
        evaluate_winner(ball, scoreboard)
    else:
        ball.forward(5)
        screen.update()

screen.exitonclick()
