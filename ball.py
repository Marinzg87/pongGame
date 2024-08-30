from turtle import Turtle


class Ball(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(starting_position)
        self.x_move = 3
        self.y_move = 3

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def refresh(self):
        self.setposition(0, 0)
        self.bounce_y()
