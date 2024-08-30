import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # detect collision with top & bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with both paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340
        or
        ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # detect when the r_paddle missed
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    # detect when the l_paddle missed
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()

screen.exitonclick()
