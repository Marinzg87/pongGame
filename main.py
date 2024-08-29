from turtle import Screen
from paddle import Paddle
from ball import Ball
STARTING_POSITION_RIGHT = (350, 10)
STARTING_POSITION_LEFT = (-350, 10)

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle(STARTING_POSITION_RIGHT)
l_paddle = Paddle(STARTING_POSITION_LEFT)
ball = Ball((0, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

screen.exitonclick()
