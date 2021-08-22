from turtle import Turtle


class Bar(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.shapesize(1, 4, 1)
        self.color("black")
        self.goto(0, -250)
        self.setheading(180)

    def move_left(self):
        self.forward(30)
    def move_right(self):
        self.backward(30)
