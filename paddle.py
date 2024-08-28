from turtle import Turtle
STARTING_POSITIONS = [(350, 10), (-350, 10)]


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.right_paddle(STARTING_POSITIONS)
        self.left_paddle(STARTING_POSITIONS)

    def right_paddle(self, position):
        paddle = Turtle("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.speed("fastest")
        paddle.goto(position[0])

    def left_paddle(self, position):
        paddle = Turtle("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.speed("fastest")
        paddle.goto(position[1])
