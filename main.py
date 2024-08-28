from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

paddle = Paddle()

screen.exitonclick()
