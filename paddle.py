from turtle import Turtle
STARTING_POSITIONS = (350, 10)
SPEED = 20


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.speed("fastest")
        self.paddle.goto(STARTING_POSITIONS)

    def go_up(self):
        new_y = self.paddle.ycor() + SPEED
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - SPEED
        self.paddle.goto(self.paddle.xcor(), new_y)
