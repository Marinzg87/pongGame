from turtle import Turtle
BALL_SPEED = 3


class Ball(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(starting_position)
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
