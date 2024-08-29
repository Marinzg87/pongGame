from turtle import Turtle
BALL_SPEED = 3


class Ball(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(starting_position)

    def move(self):
        new_x = self.xcor() + BALL_SPEED
        new_y = self.ycor() + BALL_SPEED
        self.goto(new_x, new_y)
