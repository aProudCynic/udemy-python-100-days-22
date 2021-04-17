from turtle import Screen
from constants import ARENA_WIDTH, ARENA_HEIGHT

def setup_gameplay_area(screen):
    screen.bgcolor('black')
    screen.setup(ARENA_WIDTH, ARENA_HEIGHT)
    screen.exitonclick()

screen = Screen()
setup_gameplay_area(screen)
