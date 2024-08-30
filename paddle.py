from turtle import Turtle
SPEED = 50


class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_position)
        self.points = 0

    def go_up(self):
        new_y = self.ycor() + SPEED
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - SPEED
        self.goto(self.xcor(), new_y)

    def score(self):
        self.points += 1